import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def main():
    async with streamablehttp_client(
        "http://127.0.0.1:8000/mcp"
    ) as (read_stream, write_stream, _):

        async with ClientSession(read_stream, write_stream) as session:

            await session.initialize()

            tools = await session.list_tools()

            print("Available Tools:")

            for tool in tools.tools:
                print("-", tool.name)


asyncio.run(main())