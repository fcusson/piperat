"""A Code project in bitbucket cloud"""

from piperat.core.providers.bitbucket_cloud import BitbucketCloudProvider


class BitbucketCloudProject:
    @staticmethod
    def get(
        provider: BitbucketCloudProvider,
        workspace: str,
        slug: str,
    ) -> "BitbucketCloudProject":
        """Builds a project from a provider"""
