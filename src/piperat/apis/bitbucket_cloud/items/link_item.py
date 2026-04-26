"""A link from a bitbucke cloud api response."""

from typing import TypedDict


class LinkItem(TypedDict):
    """A link from a bitbucke cloud api response."""

    href: str
    name: str
