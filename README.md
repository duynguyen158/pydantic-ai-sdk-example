# pydantic-ai-sdk-example

[![Python version](https://img.shields.io/badge/python_version-3.12-blue)](https://github.com/psf/black)

Example code getting agents & MCPs to work using Pydantic AI SDK

## Usage

**TODO: Describe how to use your project! Is it a library? A CLI? A web app?**

## Development

This project uses [uv](https://docs.astral.sh/uv/) to manage Python dependencies.

Frequently used commands or groups of commands are defined as `Makefile` recipes. Run `make help` to see a list of available recipes.

### Setting up system dependencies

Go to `shell.nix` and install listed system dependencies however you wish.

### Setting up project dependencies

It's literally as easy as

```zsh
make setup
```

### Running example scripts

1. If your script requires access to the local MCP server, start it first:

```zsh
make start-mcp-server
```

2. Scripts are located inside the `scripts` directory. For example, to run `scripts/pydantic_mcp.py`:

```zsh
uv run scripts/pydantic_mcp.py
```

#### Example results

- `/scripts/pydantic_mcp.py`

```zsh
❯ uv run scripts/pydantic_mcp.py
Result type: <class '__main__.FactsAboutDuy'>
Result: {
  "politics": true,
  "bagels": false,
  "rationale": "Duy is into politics but not bagels based on the statement \"Duy is into politics, pizzas, and the Pythagoras theorem\"."
}
Usage: RunUsage(input_tokens=2337, output_tokens=3397, requests=2)
```

- MCP server logs

```zsh
❯ make start-mcp-server
uv run pydantic_ai_sdk_example/mcp_server.py
INFO:     Started server process [34486]
INFO:     Waiting for application startup.
[08/26/25 17:44:27] INFO     StreamableHTTP session manager started                                                                                                                                                                                         streamable_http_manager.py:110
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:53826 - "POST / HTTP/1.1" 404 Not Found
[08/26/25 17:45:06] INFO     Created new transport with session ID: 95207cbc8237468f8985bd806ea27346                                                                                                                                                        streamable_http_manager.py:233
INFO:     127.0.0.1:53879 - "POST /mcp HTTP/1.1" 200 OK
INFO:     127.0.0.1:53882 - "POST /mcp HTTP/1.1" 202 Accepted
INFO:     127.0.0.1:53883 - "GET /mcp HTTP/1.1" 200 OK
INFO:     127.0.0.1:53885 - "POST /mcp HTTP/1.1" 200 OK
                    INFO     Processing request of type ListToolsRequest                                                                                                                                                                                                     server.py:624
INFO:     127.0.0.1:53935 - "POST /mcp HTTP/1.1" 200 OK
INFO:     127.0.0.1:53936 - "POST /mcp HTTP/1.1" 200 OK
INFO:     127.0.0.1:53937 - "POST /mcp HTTP/1.1" 200 OK
[08/26/25 17:45:40] INFO     Processing request of type CallToolRequest                                                                                                                                                                                                      server.py:624
INFO:     127.0.0.1:53939 - "POST /mcp HTTP/1.1" 200 OK
                    INFO     Processing request of type CallToolRequest                                                                                                                                                                                                      server.py:624
                    INFO     Processing request of type CallToolRequest                                                                                                                                                                                                      server.py:624
                    INFO     Processing request of type CallToolRequest                                                                                                                                                                                                      server.py:624
INFO:     127.0.0.1:53941 - "POST /mcp HTTP/1.1" 200 OK
                    INFO     Processing request of type ListToolsRequest                                                                                                                                                                                                     server.py:624
[08/26/25 17:46:28] INFO     Terminating session: 95207cbc8237468f8985bd806ea27346                                                                                                                                                                                  streamable_http.py:630
INFO:     127.0.0.1:53994 - "DELETE /mcp HTTP/1.1" 200 OK
[08/26/25 17:47:25] INFO     Created new transport with session ID: 64f9b1f1ea294f70ba4fa71af4609119                                                                                                                                                        streamable_http_manager.py:233
INFO:     127.0.0.1:54065 - "POST /mcp HTTP/1.1" 200 OK
INFO:     127.0.0.1:54068 - "POST /mcp HTTP/1.1" 202 Accepted
INFO:     127.0.0.1:54069 - "GET /mcp HTTP/1.1" 200 OK
INFO:     127.0.0.1:54071 - "POST /mcp HTTP/1.1" 200 OK
                    INFO     Processing request of type ListToolsRequest                                                                                                                                                                                                     server.py:624
[08/26/25 17:47:45] INFO     Terminating session: 64f9b1f1ea294f70ba4fa71af4609119                                                                                                                                                                                  streamable_http.py:630
INFO:     127.0.0.1:54095 - "DELETE /mcp HTTP/1.1" 200 OK
[08/26/25 17:48:16] INFO     Created new transport with session ID: 166c29773f1d466a935919fa0e3a9fc3                                                                                                                                                        streamable_http_manager.py:233
INFO:     127.0.0.1:54133 - "POST /mcp HTTP/1.1" 200 OK
INFO:     127.0.0.1:54136 - "POST /mcp HTTP/1.1" 202 Accepted
INFO:     127.0.0.1:54137 - "GET /mcp HTTP/1.1" 200 OK
INFO:     127.0.0.1:54139 - "POST /mcp HTTP/1.1" 200 OK
                    INFO     Processing request of type ListToolsRequest                                                                                                                                                                                                     server.py:624
INFO:     127.0.0.1:54176 - "POST /mcp HTTP/1.1" 200 OK
INFO:     127.0.0.1:54177 - "POST /mcp HTTP/1.1" 200 OK
[08/26/25 17:48:46] INFO     Processing request of type CallToolRequest                                                                                                                                                                                                      server.py:624
                    INFO     Processing request of type CallToolRequest                                                                                                                                                                                                      server.py:624
INFO:     127.0.0.1:54179 - "POST /mcp HTTP/1.1" 200 OK
                    INFO     Processing request of type ListToolsRequest                                                                                                                                                                                                     server.py:624
[08/26/25 17:49:05] INFO     Terminating session: 166c29773f1d466a935919fa0e3a9fc3                                                                                                                                                                                  streamable_http.py:630
INFO:     127.0.0.1:54201 - "DELETE /mcp HTTP/1.1" 200 OK
```

### Running tests

Run

```zsh
make test
```

to run all unit and (if available) integration tests.

### Code formatting

Applies to Python and (if applicable) Terraform code.

```zsh
make format
```

We use [Ruff](https://docs.astral.sh/ruff/) as the formatter for Python. Rules are specified in `pyproject.toml`.

### Code linting

Here, "linting" refers to the process of static-type checking in Python and (if applicable) validation of Terraform configurations.

```zsh
make lint
```

We use [Pyright](https://github.com/microsoft/pyright) as the Python static type checker. Rules are also specified in `pyproject.toml`.

## Deployment

**TODO: Describe how your project is deployed.**

_This project was created using [Duy Nguyen's cookiecutter template](https://github.com/duynguyen158/cookiecutter-python)._
