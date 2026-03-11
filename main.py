import os
from mcp.server.fastmcp import FastMCP
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.applications import Starlette
# Initialize FastMCP server
mcp = FastMCP("Render-Demo-Server")
@mcp.tool()
async def get_incidents(city: str) -> str:
    """
    Fetches the current weather for a given city.
    Args:
        city: The name of the city to check.
    """
    print("MCP Server starting get_weather...")
    return f"The weather in {city} is currently 22°C and sunny."
@mcp.tool()
def get_changerequest(a: int, b: int) -> int:
    """Adds two numbers together."""
    print("MCP Server starting add-numbers...")
    return a + b
# Get the MCP SSE app
mcp_app = mcp.sse_app()
# CRITICAL: Patch the allowed_hosts to accept any host
if isinstance(mcp_app, Starlette):
    # Disable host validation by allowing all hosts
    mcp_app.allowed_hosts = ["*"]
# Create FastAPI wrapper
api = FastAPI()
# Add CORS middleware
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Root endpoint
@api.get("/")
def root():
    return {
        "service": "ServiceNow MCP Server",
        "status": "running",
        "endpoints": {
            "health": "/health",
            "mcp_sse": "/mcp/sse",
            "mcp_messages": "/mcp/messages"
        }
    }
# Health check
@api.get("/health")
def health():
    return {"status": "healthy"}
# Mount MCP server with patched allowed hosts
api.mount("/mcp", mcp_app)
app = api
