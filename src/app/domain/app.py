from dataclasses import dataclass


@dataclass(slots=True)
class TokenInfo:
    """User information example response."""

    user: str
    uid: str


@dataclass(slots=True)
class ProjectInfo:
    """Example response data."""
    name: str
    repo_url: str
