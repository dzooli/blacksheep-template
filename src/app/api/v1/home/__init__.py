from typing import List

from app.api.common import BaseAPIController
from app.domain.common import (
    FromRemoteUserHeader,
    Scope,
    TokenInfo, SuccessResponse,
)
from blacksheep import Request
from blacksheep.server.controllers import get, post


class Home(BaseAPIController):
    """Controller for Home endpoints"""

    @classmethod
    def version(cls) -> str:
        """API version for path."""
        return "v1"

    @get(
        "/",
    )
    async def get_home(self, user: FromRemoteUserHeader) -> SuccessResponse:
        return SuccessResponse(code=200, status="OK", description="Everything is fine",
                               data=[TokenInfo(user.value, "example-UUID")])

    @post("/")
    async def create_home(self, request: Request) -> Scope:
        return Scope(request.scope.items())
