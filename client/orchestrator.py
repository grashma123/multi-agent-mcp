import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def filesystem_operation():
    async with streamablehttp_client(
        "http://127.0.0.1:8000/mcp"
    ) as (read_stream, write_stream, _):

        async with ClientSession(read_stream, write_stream) as session:

            await session.initialize()

            result = await session.call_tool(
                "get_files",
                {"path": "."}
            )

            print(result)


async def database_operation():
    async with streamablehttp_client(
        "http://127.0.0.1:8001/mcp"
    ) as (read_stream, write_stream, _):

        async with ClientSession(read_stream, write_stream) as session:

            await session.initialize()

            result = await session.call_tool(
                "get_students",
                {}
            )

            print(result)


async def main():

    while True:

        choice = input(
            "\n1. List Files\n"
            "2. Show Students\n"
            "3. Exit\n"
            "Enter choice: "
        )

        if choice == "1":
            await filesystem_operation()

        elif choice == "2":
            await database_operation()

        elif choice == "3":
            print("Goodbye")
            break

        else:
            print("Invalid choice")


asyncio.run(main())