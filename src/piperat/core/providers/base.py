"""Abstract Base Pipeline Provider class.

Classes:
    - PipelineProvider
"""

from abc import ABC, abstractmethod

from piperat.core.pipeline import Pipeline


class PipelineProvider(ABC):
    """Pipeline service provider."""

    @abstractmethod
    def get_pipelines(self) -> list[Pipeline]:
        """Provides a list of pipeline for a project."""
