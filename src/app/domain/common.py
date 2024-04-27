from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List, Union

from blacksheep import FromHeader

from .app import ProjectInfo, TokenInfo
from .internal import Scope


class FromRemoteUserHeader(FromHeader[str]):
    name = "Remote-User"


class ResponseStatus(Enum):
    """Common response status strings."""
    OK: str = "OK"
    ERROR: str = "ERROR"
    FAILURE: str = "FAILURE"


@dataclass(slots=True)
class ErrorResponse:
    """Example response.

    Usable as error response.
    """

    code: int = 400
    status: ResponseStatus = "ERROR"
    description: Optional[str] = field(init=True, default=None, kw_only=True)
    details: Optional[str] = field(init=True, default=None, kw_only=True)


@dataclass(slots=True)
class SuccessResponse(ErrorResponse):
    """Example success response.

    Almost same as ErrorResponse but should be initialized
    with another status code and has an additional ```data``` field
    with proper Swagger doc generation.
    """
    code: int = field(default=200)
    status: ResponseStatus = field(default=ResponseStatus.OK)
    data: Optional[List[Union[TokenInfo, ProjectInfo, Scope]]] = None


@dataclass(slots=True)
class HomeSuccessResponse(SuccessResponse):
    data: Optional[List[TokenInfo]] = None

