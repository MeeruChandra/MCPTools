import os
from mcp.server.fastmcp import FastMCP
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
# 1. Initialize FastMCP with proper configuration
mcp = FastMCP("Render-Demo-Server")
@mcp.tool()
async def get_incidents(city: str) -> str:
    """Fetches weather for a city."""
    return f"The weather in {city} is currently 22°C and sunny."
@mcp.tool()
def get_changerequest(a: int, b: int) -> int:
    """Adds two numbers together."""
    return a + b
# 2. Create FastAPI app
app = FastAPI()
# Add CORS - required for SSE
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],  # Important for SSE
)
@app.get("/")
async def root():
    return {"message": "MCP Server is running", "sse_endpoint": "/sse"}
# 3. Mount MCP at root level instead of /mcp
app.mount("", mcp.get_asgi_app())
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 10000))
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=port,
        log_level="info"
    )
