import os
import json
from google.adk.agents import Agent
from google.adk.tools.openapi_tool.openapi_spec_parser.openapi_toolset import OpenAPIToolset
# We will need different auth helpers for OAuth 2.0
# from google.adk.tools.openapi_tool.auth.auth_helpers import token_to_scheme_credential
from fastapi.openapi.models import OAuth2, OAuthFlows, OAuthFlowAuthorizationCode
from google.adk.auth import AuthCredential, AuthCredentialTypes, OAuth2Auth
import logging
import sys

# Configure basic logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("gdrive_agent")

# Define both gdrive_agent and root_agent (ADK framework looks for root_agent)
gdrive_agent = None
root_agent = None

def load_api_spec(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading API spec: {e}")
        return None

# TODO: Obtain these from Google Cloud Console and store securely (e.g., env variables)
YOUR_OAUTH_CLIENT_ID = os.getenv("GDRIVE_CLIENT_ID", "YOUR_CLIENT_ID_HERE")
YOUR_OAUTH_CLIENT_SECRET = os.getenv("GDRIVE_CLIENT_SECRET", "YOUR_CLIENT_SECRET_HERE")

def create_gdrive_agent(api_spec_path=os.path.join(os.path.dirname(__file__), "..", "google_drive_v3_openapi.json")):
    if not os.path.exists(api_spec_path):
        logger.error(f"Google Drive API spec file not found: {api_spec_path}")
        return None

    spec = load_api_spec(api_spec_path)
    if not spec:
        return None

    try:
        # Define OAuth 2.0 Authorization Code Flow
        # These URLs are standard for Google APIs
        auth_scheme = OAuth2(
            flows=OAuthFlows(
                authorizationCode=OAuthFlowAuthorizationCode(
                    authorizationUrl="https://accounts.google.com/o/oauth2/auth",
                    tokenUrl="https://oauth2.googleapis.com/token",
                    scopes={  # Example scopes - adjust as needed for desired functionality
                        "https://www.googleapis.com/auth/drive.metadata.readonly": "View metadata for files in your Google Drive",
                        "https://www.googleapis.com/auth/drive.file": "View and manage Google Drive files and folders that you have opened or created with this app",
                        "https://www.googleapis.com/auth/drive.readonly": "View all your Google Drive files (read-only)",
                        # Add more scopes as required by the user's needs (e.g., full drive access, specific file types)
                    },
                )
            )
        )

        # Define the initial credentials for your application
        auth_credential = AuthCredential(
            auth_type=AuthCredentialTypes.OAUTH2,
            oauth2=OAuth2Auth(
                client_id=YOUR_OAUTH_CLIENT_ID,
                client_secret=YOUR_OAUTH_CLIENT_SECRET
                # redirect_uri will be handled by the ADK flow or client application
            ),
        )

        if YOUR_OAUTH_CLIENT_ID == "YOUR_CLIENT_ID_HERE" or YOUR_OAUTH_CLIENT_SECRET == "YOUR_CLIENT_SECRET_HERE":
            logger.warning("Using placeholder Client ID or Secret. Please set GDRIVE_CLIENT_ID and GDRIVE_CLIENT_SECRET environment variables.")

        toolset = OpenAPIToolset(
            spec_str=json.dumps(spec),
            spec_str_type="json",
            auth_scheme=auth_scheme,
            auth_credential=auth_credential
        )

        tools = toolset.get_tools()
        if not tools:
            logger.error("No tools found in Google Drive API spec")
            return None

        logger.info(f"Found {len(tools)} Google Drive API tools")

        return Agent(
            name="gdrive_agent",
            description="Google Drive API Agent",
            instruction="""
            You are a Google Drive API agent that interacts with Google Drive.
            You can perform operations like listing files, getting file details, managing metadata, checking for duplicates, and other actions supported by the Google Drive API.

            When working with the Google Drive API:
            - Use parameters provided by the user.
            - Ask for clarification if required parameters are missing for an operation.
            - Format responses clearly for the user.
            - Handle errors gracefully and explain issues in simple terms.
            - If authentication is required and not yet performed, the system will guide the user through the OAuth 2.0 flow.

            Always inform the user about the actions you're taking and the results received.
            """,
            model="gemini-2.5-pro-preview-03-25", # Or your preferred model
            tools=tools
        )
    except Exception as e:
        logger.error(f"Error creating Google Drive agent: {e}")
        # import traceback
        # traceback.print_exc() # Uncomment for detailed error during development
        return None

# Create the agent with Google Drive configuration
gdrive_agent = create_gdrive_agent()

# Set root_agent to gdrive_agent for compatibility with ADK framework
root_agent = gdrive_agent

if gdrive_agent:
    logger.info("Google Drive agent created successfully (initialization).")
    logger.info("Note: OAuth 2.0 authentication flow will be initiated when a protected API is called.")
    # To see available tools (optional, can be very long for Drive API):
    # logger.info("Available Google Drive tools:")
    # for tool in gdrive_agent.tools:
    #     logger.info(f"• {tool.name}")
else:
    logger.error("Failed to create Google Drive agent.")
    sys.exit(1)
