# Program:
from fastmcp import FastMCP
import json

mcp = FastMCP(name="RemoteMCP")

@mcp.tool
def add_nums(a:float, b:float) ->float:
    """Add two numbers together."""
    return a + b


@mcp.resource("info://server")
def server_info() -> str:
    """Get information about this server."""
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A basic MCP server with math tools",
        "tools": ["add_nums"],
        "author": "maroofgadiwale"
    }
    return json.dumps(info, indent=2)

if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)
