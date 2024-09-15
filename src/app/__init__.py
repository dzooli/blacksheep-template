"""Application package.

Modules:
    server:         Main entry point
    api.common:     Common classes and functions for the API endpoints
    api.v1:         Endpoint handlers for API version v1
"""

import inspect
import unittest.mock
from functools import wraps
from typing import (
    Any,
    Awaitable,
    Callable,
)

import orjson
from app import __about__
from blacksheep import Application, json
from blacksheep.messages import Request, Response
from blacksheep.server.normalization import ensure_response
from blacksheep.server.openapi.v3 import OpenAPIHandler
from blacksheep.server.rendering.jinja2 import JinjaRenderer
from blacksheep.settings.html import html_settings
from blacksheep.settings.json import json_settings
from openapidocs.v3 import Info, License


class BaseApplication(Application):
    """Customized Blacksheep Application class.

    Contains an error handler for unhandled exceptions.
    """

    @classmethod
    async def handle_internal_server_error(cls, request: Request, exc: Exception) -> Response:
        """Handles the unhandled exception.

        Args:
            request (Request): Blacksheep request
            exc (Exception): Exception to handle

        Returns:
            Response: A JSON response string with exception details and status code 500
        """
        return json({"status": "FAILED", "error": str(exc.__class__), "message": str(exc)}, 500)


def _get_async_wrapper_for_output_patched(
    method: Callable[[Request], Any],
) -> Callable[[Request], Awaitable[Response]]:
    """A patch for Blacksheep"""

    @wraps(method)
    async def handler(request: Request) -> Response:
        response = await method(request)
        # Handle consequences of @validate_arguments decorator applied to async code
        if inspect.isawaitable(response):
            response = await response
        return ensure_response(response)

    return handler


async_wrapper = unittest.mock.patch(
    "blacksheep.server.normalization._get_async_wrapper_for_output",
    _get_async_wrapper_for_output_patched,
)
async_wrapper.start()


def orjson_serialize(value) -> str:
    """Using json serializer from orjson package for faster serialization."""
    return orjson.dumps(value).decode("utf-8")


json_settings.use(loads=orjson.loads, dumps=orjson_serialize)

html_settings.use(JinjaRenderer(enable_async=True))

docs = OpenAPIHandler(
    info=Info(
        title=__about__.__title__,
        version=__about__.__version__,
        description=__about__.__doc__,
        license=License(__about__.__license__, __about__.__license_url__),
    )
)
