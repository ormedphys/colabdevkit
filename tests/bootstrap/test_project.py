"""
Tests for bootstrap.project.
"""

from pathlib import Path

from colabdevkit.bootstrap.project import (
    change_directory,
    project_exists,
    project_root,
)


def test_project_exists():
    assert project_exists(".") is True
    assert project_exists("arquivo_inexistente") is False


def test_project_root():
    root = project_root(".")

    assert isinstance(root, Path)
    assert root.exists()


def test_change_directory():
    root = project_root(".")

    current = change_directory(root)

    assert current == Path.cwd()
    assert current == root
