
"""
Project bootstrap helpers.
"""

from pathlib import Path


def project_exists(path: str | Path) -> bool:
    """
    Returns True if a project directory exists.
    """
    return Path(path).exists()
    