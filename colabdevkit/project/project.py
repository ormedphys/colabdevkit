"""Project abstraction."""

from pathlib import Path


class Project:
    """Represent a ColabDevKit project."""

    def __init__(self, root: str | Path):
        """Initialize a project representation.

        Parameters
        ----------
        root
            Project root directory.
        """
        self._root = Path(root).expanduser().resolve()

    @property
    def root(self) -> Path:
        """Return the absolute project root."""
        return self._root

    @property
    def name(self) -> str:
        """Return the project name."""
        return self._root.name

    def exists(self) -> bool:
        """Return True if the project root exists."""
        return self._root.exists()
