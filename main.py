import os
from mcp.server.fastmcp import FastMCP
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
# Custom middleware to handle host header
class HostHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Allow any host
        request.scope["server"] = ("0.0.0.0", int(os.getenv("PORT", 8000)))
        response = await call_next(request)
        return response
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
# Create FastAPI wrapper with disabled docs (optional but helps)
api = FastAPI(docs_url=None, redoc_url=None)
# Add host header middleware FIRST
api.add_middleware(HostHeaderMiddleware)
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
api.mount("/mcp", mcp.sse_app())
app = api
