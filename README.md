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

Scripts are located inside the `scripts` directory. For example, to run `scripts/pydantic_mcp.py`:

```zsh
uv run scripts/pydantic_mcp.py
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
