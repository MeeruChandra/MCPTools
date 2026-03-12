import os
from mcp.server.fastmcp import FastMCP
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# 1. Initialize FastMCP
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
)

# Root route so you don't get "Not Found" when testing the base URL
@app.get("/")
async def root():
    return {"message": "MCP Server is running", "endpoint": "/mcp/sse"}

# 3. Mount MCP
# We mount it to /mcp. This creates /mcp/sse and /mcp/messages
app.mount("/mcp", mcp.sse_app())

if __name__ == "__main__":
    import uvicorn
    # Render dynamic port
    port = int(os.getenv("PORT", 1000))
    # host MUST be 0.0.0.0 for Render to expose the service
    uvicorn.run(app, host="0.0.0.0", port=port)
