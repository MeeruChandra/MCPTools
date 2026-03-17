import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my_echo_server")

@mcp.tool()
def echo(text: str) -> str:
    return text + " From My Test server"

