import os
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
# The name will appear in your AI client's UI
mcp = FastMCP("Render-Demo-Server")

@mcp.tool()
async def get_weather(city: str) -> str:
    """
    Fetches the current weather for a given city.
    Args:
        city: The name of the city to check.
    """
    # In a real app, you'd use httpx to call a weather API
    print("MCP Server starting get_weather...")
    return f"The weather in {city} is currently 22°C and sunny."

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers together."""
    print("MCP Server starting add-numbers...")
    return a + b

app = mcp.sse_app()

# if __name__ == "__main__":
#     # Render provides a PORT environment variable automatically
#     port = int(os.environ.get("PORT", 8000))
#     # Use SSE transport for remote web deployment
#     #mcp.run(transport="sse")

#     #if __name__ == "__main__":

#     mcp.run(
#         transport="sse",
#         host="0.0.0.0",
#         port=port
#     )