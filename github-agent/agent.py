import os
import json
from google.adk.agents import Agent
from google.adk.tools.openapi_tool.openapi_spec_parser.openapi_toolset import OpenAPIToolset
from google.adk.tools.openapi_tool.auth.auth_helpers import token_to_scheme_credential
import logging
import sys

# Configure basic logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("github_agent")

# Define both github_agent and root_agent (ADK framework looks for root_agent)
github_agent = None
root_agent = None

def load_api_spec(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading API spec: {e}")
        return None

def create_github_agent(api_spec_path=os.path.join(os.path.dirname(__file__), "api.github.com.fixed.json"), token_env_var="GITHUB_TOKEN", auth_prefix="token"):
    token = os.getenv(token_env_var)
    if not token:
        logger.error(f"GitHub token missing from environment variable: {token_env_var}")
        return None
        
    if not os.path.exists(api_spec_path):
        logger.error(f"GitHub API spec file not found: {api_spec_path}")
        return None
        
    spec = load_api_spec(api_spec_path)
    if not spec:
        return None
        
    try:
        auth_scheme, auth_credential = token_to_scheme_credential(
            "apikey", "header", "Authorization", f"{auth_prefix} {token}"
        )
        
        toolset = OpenAPIToolset(
            spec_str=json.dumps(spec),
            spec_str_type="json",
            auth_scheme=auth_scheme,
            auth_credential=auth_credential
        )
        
        tools = toolset.get_tools()
        if not tools:
            logger.error("No tools found in GitHub API spec")
            return None
            
        logger.info(f"Found {len(tools)} GitHub API tools")
        
        return Agent(
            name="github_agent",
            description="GitHub API Agent",
            instruction="""
            You are a GitHub API agent that interacts with GitHub's REST API.
            
            When working with the GitHub API:
            - Use parameters provided by the user
            - Ask for clarification if required parameters are missing
            - Format responses clearly for the user
            - Handle errors gracefully and explain issues in simple terms
            
            For content creation operations:
            - Use names and identifiers exactly as specified by the user
            - Add helpful descriptions when allowed by the API
            - Apply sensible defaults for optional parameters when not specified
            
            Always inform the user about the actions you're taking and the results received.
            """,
            model="gemini-2.5-pro-preview-03-25",
            tools=tools
        )
    except Exception as e:
        logger.error(f"Error creating GitHub agent: {e}")
        return None

# Create the agent with GitHub configuration as default
github_agent = create_github_agent()

# Set root_agent to github_agent for compatibility with ADK framework
root_agent = github_agent

if github_agent:
    logger.info("GitHub agent created successfully")
    # Print available tools
    for tool in github_agent.tools:
        print(f"• {tool.name}")
else:
    logger.error("Failed to create GitHub agent")
    sys.exit(1)


