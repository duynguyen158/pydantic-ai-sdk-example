from mcp.server.fastmcp import FastMCP

app = FastMCP()


@app.tool()
def stuff_duy_is_into() -> str:
    return "Duy is into politics, pizza, and the Pythagoras theorem."


@app.tool()
def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    app.run(transport="streamable-http")
