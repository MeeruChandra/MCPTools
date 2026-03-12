import os
from mcp.server.fastmcp import FastMCP
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

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

# Create FastAPI app
app = FastAPI()

# Add CORS middleware - Essential for SSE and cross-origin MCP clients
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check for Render
@app.get("/health")
def health():
    return {"status": "running"}

# Mount MCP server
# Use the direct sse_app() mounting
app.mount("/mcp", mcp.sse_app())

if __name__ == "__main__":
    import uvicorn
    # Render provides the PORT env var automatically
    port = int(os.environ.get("PORT", 1000))
    uvicorn.run(app, host="0.0.0.0", port=port)
