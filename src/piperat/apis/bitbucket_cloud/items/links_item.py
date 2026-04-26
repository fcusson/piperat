"""Series of links from an object from a bitbucket cloud api response."""

from typing import TypedDict, Optional

from .link_item import LinkItem


class LinksItem(TypedDict):
    """Series of links from an object from a bitbucket cloud api response."""

    self: Optional[LinkItem]
    html: Optional[LinkItem]
    avatar: LinkItem
    pullrequests: Optional[LinkItem]
    commits: Optional[LinkItem]
    forks: Optional[LinkItem]
    watchers: Optional[LinkItem]
    downloads: Optional[LinkItem]
    clone: Optional[LinkItem]
    hooks: Optional[LinkItem]
