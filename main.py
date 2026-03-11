from mcp.server.fastmcp import FastMCP
from fastapi import FastAPI
from starlette.middleware.trustedhost import TrustedHostMiddleware

mcp = FastMCP("Render-Demo-Server")

@mcp.tool()
async def get_incidents(city: str) -> str:
    return f"The weather in {city} is currently 22°C and sunny."

@mcp.tool()
def get_changerequests(a: int, b: int) -> int:
    return a + b

# Create FastAPI wrapper
api = FastAPI()

# Allow Render host
api.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"]   # or ["servicenowtool.onrender.com"]
)

# Mount MCP server
api.mount("/", mcp.sse_app())

app = api
