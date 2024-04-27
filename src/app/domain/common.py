from dataclasses import dataclass

from _collections_abc import dict_items
from typing import Any, Optional, List, Union

from blacksheep import FromHeader


class FromRemoteUserHeader(FromHeader[str]):
    name = "Remote-User"


@dataclass
class Scope:
    def __init__(self, items: dict_items):
        for k, v in items:
            setattr(self, k, str(v))


@dataclass(slots=True)
class TokenInfo:
    """User information example."""

    user: str
    uid: str


@dataclass(slots=True)
class ProjectInfo:
    name: str
    repo_url: str


@dataclass(slots=True)
class ErrorResponse:
    """Example response.

    Usable for a common response or as an error response.
    """

    code: int
    status: str
    description: Optional[str] = None
    details: Optional[str] = None


@dataclass(slots=True)
class SuccessResponse(ErrorResponse):
    data: Optional[List[Union[TokenInfo, ProjectInfo]]] = None
