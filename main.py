import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my_echo_server")

@mcp.tool()
def echo(text: str) -> str:
    return text + " From My Test server"

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000))
    )
