"""Abstract Base Pipeline Provider class.

Classes:
    - PipelineProvider
"""

from abc import ABC, abstractmethod


class PipelineProvider(ABC):
    """Pipeline service provider."""

    @abstractmethod
    def foo(self) -> None:
        """Dummy class for lint passing."""
