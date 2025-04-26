"""Bitbucket pipeline provider.

Classes:
    BitbucketProvider
"""

from atlassian.bitbucket.cloud import Cloud

from piperat.providers.base import PipelineProvider


class BitbucketCloudProvider(PipelineProvider):
    """Bitucket Cloud Pipeline provider."""

    def __init__(self, username: str, password: str):
        """Bitbucket Cloud Pipeline provider."""
        self._client: Cloud = Cloud(
            username=username,
            password=password,
        )

        self._client.repositories.get("brotherca-ai", "aws-utils")

    def foo(self) -> None:
        """Dummy implementation."""


if __name__ == "__main__":
    username = "felix.cusson@brother.ca"
