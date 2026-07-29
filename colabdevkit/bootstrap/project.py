
"""
Project bootstrap helpers.
"""

from pathlib import Path


def project_exists(path: str | Path) -> bool:
    """
    Returns True if the project directory exists.
    """
    return Path(path).exists()
