# Blacksheep API template

## Description

A template for Blacksheep-based API with the following features:

- Flexible package manager: [hatch](https://hatch.pypa.io/latest/), poetry or pip
- Separated requirements.txt files for the app, for development and for documentation.
- Using environment variables for separated development and production execution
- Unit-testing setup with working autodiscovery in VSCode
- Swagger UI on /docs endpoint
- Path-based API versioning
- Class-based views and endpoints
- Response types based on ```dataclasses.dataclass```
- Fast JSON serializer using [orjson](https://github.com/ijl/orjson)
- Async template rendering
- Built-in anti-forgery (commented out in server.py)
- MkDocs for documentation
    - Automated source code docstring extraction
    - API documentation from openapi.json - needs to be saved before
    - Clear structure

## Usage

With ```hatch```:

- Start dev server
    ```shell
    hatch run serve
    ```

- Run tests
    ```shell
    hatch run test
    ```

- Run tests with coverage measurement
    ```shell
    hatch run test-cov
    ```
- Generate coverage report (lcov and xml, usable with coverage-gutters VSCode extension)
    ```shell
    hatch run cov
    ```
- Doc development with live reload
    ```shell
    hatch run doc:serve
    ```
- Build the docs into ./build/docs
    ```shell
    hatch run doc:build
    ```
- Format check (ruff)
    ```shell
    hatch fmt --check
    ```
- Formatting
    ```shell
    hatch fmt
    ```
- Build wheels and sdist packages
    ```shell
    hatch build
    ```

## Debug setup

With VSCode use the following ```launch.json```:

```json5
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Server",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/src/app/server.py",
            "console": "integratedTerminal",
            //"args": "${command:pickArgs}",
            "env": {
                "APP_ENV": "dev",
                "PYTHONPATH": "${workspaceFolder}/src"
            }
        }
    ]
}
```

## Contribution

Create your fork and submit pull-requests.
