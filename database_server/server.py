from mcp.server.fastmcp import FastMCP
from tools import create_table, insert_student, list_students

mcp = FastMCP("Database Server")


@mcp.tool()
def create_students_table():
    return create_table()


@mcp.tool()
def add_student(name: str, age: int):
    return insert_student(name, age)


@mcp.tool()
def get_students():
    return list_students()


if __name__ == "__main__":
    print("Database MCP Server Running...")
    mcp.settings.port = 8001
    mcp.run(transport="streamable-http")