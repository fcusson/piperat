"""Bitbucket pipeline provider.

Classes:
    BitbucketProvider
"""

from itertools import islice

from atlassian.bitbucket.cloud import Cloud

from piperat.core.pipeline import Pipeline
from piperat.core.providers.base import PipelineProvider


class BitbucketCloudProvider(PipelineProvider):
    """Bitucket Cloud Pipeline provider."""

    def __init__(self, username: str, password: str):
        """Bitbucket Cloud Pipeline provider."""
        self._client: Cloud = Cloud(
            username=username,
            password=password,
        )

        self._client.repositories.get("brotherca-ai", "aws-utils")

    def get_pipelines(self, project, count: int) -> list[Pipeline]:
        """Provides a list of available pipelines for a project."""

        pipelines = self._client.repositories.get(
            "brotherca-ai", "aws-utils"
        ).pipelines.each(sort="-created_on", q="pagelen=10")

        pipelines = list(islice(pipelines, 10))

        return []


if __name__ == "__main__":
    username = "fcusson"
    password = "REDACTED"

    provider = BitbucketCloudProvider(username, password)
    provider.get_pipelines()
