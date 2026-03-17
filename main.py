from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("my_echo_server", port="8000")

@mcp.tool()
def echo(text: str) -> str:
    """Echo the provided text back to the caller"""
    return text + " From My Test server"

#if __name__ == "__main__":
    #mcp.run()  # STDIO mode by default

if __name__ == "__main__":
    #mcp.run(transport="streamable-http")
    mcp.run(transport="sse")
