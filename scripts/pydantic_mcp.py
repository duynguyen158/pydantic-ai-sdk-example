"""Adapted from: https://ai.pydantic.dev/examples/pydantic-model/#example-code"""

import asyncio

from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.ollama import OllamaProvider


class Output(BaseModel):
    city: str
    country: str


async def main() -> None:
    model = OpenAIChatModel(
        model_name="qwen3:4b-thinking-2507-q4_K_M",
        provider=OllamaProvider(base_url="http://localhost:11434/v1"),
    )
    agent = Agent(model, output_type=Output)

    result = await agent.run("The windy city in the US of A.")
    print("Result type:", type(result.output))
    print("Result:", result.output.model_dump_json(indent=2))
    print("Usage:", result.usage())


if __name__ == "__main__":
    asyncio.run(main())
