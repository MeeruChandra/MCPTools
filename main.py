import os
from mcp.server.fastmcp import FastMCP
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
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
# Patch the allowed hosts
if hasattr(mcp_app, 'allowed_hosts'):
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
# Health check
@api.get("/health")
def health():
    return {"status": "running"}
# Mount MCP server
api.mount("/mcp", mcp_app)
app = api
