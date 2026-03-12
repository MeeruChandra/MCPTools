import os
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Render-Demo-Server")

@mcp.tool()
async def get_incidents(city: str) -> str:
    """Fetches weather (simulated incidents) for a city."""
    return f"The weather in {city} is currently 22°C and sunny."

@mcp.tool()
def get_changerequest(a: int, b: int) -> int:
    """Adds two numbers together."""
    return a + b

if __name__ == "__main__":
    # FastMCP.run() automatically handles the SSE server setup
    # and correctly configures the ASGI scope validation.
    port = int(os.getenv("PORT", 1000))
    mcp.run(transport="sse", host="0.0.0.0", port=port)
