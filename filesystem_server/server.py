from mcp.server.fastmcp import FastMCP
from tools import list_files, read_file

mcp = FastMCP("Filesystem Server")

@mcp.tool()
def get_files(path: str = "."):
    return list_files(path)

@mcp.tool()
def get_file_content(filename: str):
    return read_file(filename)

if __name__ == "__main__":
    print("MCP Server Running...")
    mcp.run(transport="streamable-http")