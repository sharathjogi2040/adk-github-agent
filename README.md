# GitHub Agent with Google ADK and OpenAPI Tools

A powerful GitHub automation agent built using Google's Agent Development Kit (ADK) and OpenAPI Specification tools that provides a natural language interface to GitHub's REST API.

## Table of Contents

- [Introduction](#introduction)
- [Demo](#demo)
- [Architecture](#architecture)
  - [Core Components](#core-components)
  - [Workflow](#workflow)
- [How OpenAPI Tools Work in ADK](#how-openapi-tools-work-in-adk)
  - [Key Components](#key-components)
  - [How It Works](#how-it-works)
- [Implementation Guide](#implementation-guide)
  - [Prerequisites](#prerequisites)
  - [Project Structure](#project-structure)
  - [Setup Instructions](#setup-instructions)
  - [Implementation Highlights](#implementation-highlights)
- [Resources](#resources)
- [Usage Examples](#usage-examples)
- [GitHub Repository](#github-repository)

## Introduction

This project demonstrates how to build an AI-powered GitHub agent using Google's [Agent Development Kit (ADK)](https://google.github.io/adk-docs/) and OpenAPI integration. The agent leverages the GitHub REST API through an OpenAPI specification to perform various GitHub operations via natural language commands.

Agent Development Kit (ADK) supports a wide range of tool integrations for building agents, including Function tools, Built-in tools, Third party tools, Google Cloud Tools, MCP Tools, and OpenAPI tools with support for Authentication. This project focuses on how to integrate REST APIs using OpenAPI specification, eliminating the need to manually define individual function tools for each API endpoint.

## Demo

![GitHub Agent in Action](./Images/adk-web-github-agent-openspec.gif)

![GitHub Agent API Demo](./Images/adk-github-agent-openapispec.gif)

## Architecture

![Architecture Diagram](./Images/adk-github-agent.png)

### Core Components:

* **[Google ADK](https://google.github.io/adk-docs/)** — Provides the agent framework and infrastructure (Agent class)
* **[OpenAPI Tools](https://google.github.io/adk-docs/tools/openapi-tools/)** — Transforms API specifications into executable tools
* **OpenAPI Specification** — GitHub's v3 API defined in JSON format
* **Authentication Handler** — Manages GitHub personal access tokens
* **Gemini 2.5 Pro** — Powers the language understanding & generation
* **OpenAPIToolset** — Dynamically generates API tools from the spec

### Workflow:

1. **Query Input**: User enters a natural language request (e.g., "show my repositories")
2. **Initial Processing**:
   * The query is routed to the GitHub agent
   * ADK prepares the context including the API spec and auth token
3. **LLM Processing**:
   * Gemini 2.5 Pro interprets the user's intent
   * The query is mapped to potential GitHub API operations
4. **Tool Discovery**:
   * OpenAPIToolset identifies relevant API endpoints
   * Parameters are extracted or requested if missing
5. **API Execution**:
   * The selected GitHub API is called with proper authentication
   * The operation executes against GitHub's servers
6. **Response Handling**:
   * API response is formatted for readability
   * Results are presented back to the user

## How OpenAPI Tools Work in ADK

The [OpenAPI Tools in ADK](https://google.github.io/adk-docs/tools/openapi-tools/) provide a powerful way to integrate REST APIs with your agent:

### Key Components

1. **`OpenAPIToolset`**: The primary class that handles parsing an OpenAPI specification and generating tools from it. You initialize it with your OpenAPI specification, and it takes care of turning API operations into callable tools.

2. **`RestApiTool`**: Represents a single API operation (like `GET /repos/{owner}/{repo}` or `POST /repos`). The `OpenAPIToolset` creates one `RestApiTool` for each operation defined in your spec.

### How It Works

The process follows these main steps:

1. **Initialization & Parsing**:
   * You provide the GitHub API OpenAPI specification to `OpenAPIToolset` (as JSON in our case)
   * The toolset parses the spec, resolving any internal references to understand the complete API structure

2. **Operation Discovery**:
   * It identifies all valid API operations (GET, POST, PUT, DELETE) defined within the `paths` section
   
3. **Tool Generation**:
   * For each discovered operation, a corresponding `RestApiTool` is created
   * Tool names are derived from the `operationId` in the spec (converted to snake_case)
   * Tool descriptions come from the `summary` or `description` fields to help the LLM understand
   * API details (method, path, parameters, request body schema) are stored internally

4. **Tool Functionality**:
   * Each tool dynamically creates a function schema based on the operation's parameters
   * When called by the LLM, it constructs the correct HTTP request using the provided arguments
   * It handles authentication and executes the API call to GitHub
   * Returns the API response back to the agent

5. **Authentication**:
   * The GitHub token is configured during toolset initialization
   * Authentication is automatically applied to all generated tools

## Implementation Guide

This section provides a step-by-step guide to setting up and using the GitHub agent.

### Prerequisites

1. **Python 3.11+** installed
2. **Google Gemini Generative AI** access via API key
3. **GitHub account** and personal access token
4. **GitHub OpenAPI Spec**: [GitHub REST API Description](https://raw.githubusercontent.com/github/rest-api-description/main/descriptions/api.github.com/api.github.com.json)

### Project Structure

- `github-agent/agent.py`: Main agent implementation
- `github-agent/api.github.com.fixed.json`: GitHub API OpenAPI specification

## Features

- Interact with GitHub's REST API using natural language
- Perform GitHub operations without knowing the specific API endpoints
- Authenticated access to GitHub repositories and resources
- AI-powered interface using Gemini 2.5 Pro

## Prerequisites

- Python 3.11 or higher
- A GitHub personal access token

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/arjunprabhulal/adk-github-agent.git
   cd adk-github-agent
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install google-adk
   ```

4. Obtain a GitHub API token:
   - Go to GitHub → Settings → Developer settings → Personal access tokens
   - Generate a new token with appropriate permissions
   - Save the token securely for use in your application

5. Set your GitHub token as an environment variable:
   ```bash
   export GITHUB_TOKEN=your_github_token_here
   ```

6. Run the agent:
   ```bash
   adk web
   ```

## Usage

Run the agent from the github-agent directory:

```bash
cd github-agent
adk web
```

## Example Interactions

- "Create a new repository named 'my-project'"
- "List all my repositories"
- "Create an issue in repo X with title Y"
- "Add a comment to issue #123"

## License

MIT

## Acknowledgements

Built with [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/)

### Implementation Highlights

The GitHub agent is built using the following key components from ADK:

1. **Agent**: The core building block of ADK that provides LLM integration, conversation management, tool orchestration, and prompt management.

2. **OpenAPIToolset**: Transforms API specifications into executable tools:
   - Reads and interprets GitHub's OpenAPI specification JSON
   - Automatically creates tools for each API endpoint (over 1000+ GitHub operations)
   - Manages required/optional parameters for API calls
   - Formats API responses for user consumption

3. **Authentication**: Uses the `token_to_scheme_credential` function to:
   - Convert raw GitHub token to proper authorization format
   - Configure header-based API key authentication
   - Create credentials object used by the OpenAPIToolset
   - Format token with "token" prefix required by GitHub

## Resources

- [Google Agent Development Kit Documentation](https://google.github.io/adk-docs/)
- [OpenAPI Tools in ADK](https://google.github.io/adk-docs/tools/openapi-tools/)

## Usage Examples

Try interacting with the agent using natural language commands like:
- "List my repositories"
- "Create a new repository named test-repo"
- "Create a new issue in repository X titled 'Feature request'"
- "What are the open pull requests in my repositories?"

## GitHub Repository

You can access all the code used in this project at:
[github.com/arjunprabhulal/adk-github-agent](https://github.com/arjunprabhulal/adk-github-agent) 