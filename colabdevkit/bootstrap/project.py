"""
Project bootstrap helpers.
"""

import os
from pathlib import Path


def project_exists(path: str | Path) -> bool:
    """
    Returns True if the project directory exists.
    """

    return Path(path).exists()


def project_root(path: str | Path) -> Path:
    """
    Return the absolute path of the project root.

    Parameters
    ----------
    path
        Project directory.

    Returns
    -------
    Path
        Absolute project path.

    Raises
    ------
    FileNotFoundError
        If the project directory does not exist.
    """

    path = Path(path).expanduser().resolve()

    if not path.exists():
        raise FileNotFoundError(path)

    return path


def change_directory(path: str | Path) -> Path:
    """
    Change the current working directory.

    Parameters
    ----------
    path
        Destination directory.

    Returns
    -------
    Path
        New current working directory.
    """

    root = project_root(path)

    os.chdir(root)

    return Path.cwd()
