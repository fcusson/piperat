"""Typed Dictionary of the GetRepository api response."""

from piperat.apis.bitbucket_cloud.items.links_item import LinksItem
from .base import BitbucketCloudResponse


class GetRepositoryResponse(BitbucketCloudResponse):
    """Typed Dictionary of the GetRepository api response."""

    links: LinksItem
    uuid: str
    full_name: str
    is_private: bool
    scm: str
