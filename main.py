import os
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("My Render Server")

@mcp.tool()
def greet(name: str) -> str:
    """A simple tool to greet the user."""
    return f"Hello, {name}! This is running on Render!"

if __name__ == "__main__":
    # Render provides a 'PORT' environment variable
    port = int(os.getenv("PORT", 8000))
    
    # Use transport="sse" to expose via HTTP/SSE
    # host="0.0.0.0" is required for Render to route traffic to your container
    mcp.run(transport="sse", host="0.0.0.0", port=port)
