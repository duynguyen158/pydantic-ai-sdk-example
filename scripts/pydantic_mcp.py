"""Adapted from: https://ai.pydantic.dev/examples/pydantic-model/#example-code"""

import asyncio
from typing import Annotated

from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStreamableHTTP
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.ollama import OllamaProvider


class FactsAboutDuy(BaseModel):
    politics: Annotated[bool, Field(description="Is Duy into politics?")]
    bagels: Annotated[bool, Field(description="Is Duy into bagels?")]
    addition: Annotated[
        bool, Field(description="Use the add tool to tell me the sum of 451 and 227.")
    ]
    rationale: Annotated[
        str,
        Field(
            description="Explain, in a few sentences, your thinking in answering the questions above."
        ),
    ]


async def main() -> None:
    server = MCPServerStreamableHTTP(url="http://localhost:8000")
    # Ollama's API is OpenAI-compatible
    model = OpenAIChatModel(
        model_name="qwen3:4b-thinking-2507-q4_K_M",
        provider=OllamaProvider(base_url="http://localhost:11434/v1"),
    )
    agent = Agent(
        model,
        output_type=FactsAboutDuy,
        system_prompt="You are a Gen Z assistant. Answer questions as provided and append three emojis to end of each of your answers.",
        toolsets=[server],
    )

    async with agent:
        result = await agent.run("The windy city in the US of A.")

    print("Result type:", type(result.output))
    print("Result:", result.output.model_dump_json(indent=2))
    print("Usage:", result.usage())


if __name__ == "__main__":
    asyncio.run(main())
