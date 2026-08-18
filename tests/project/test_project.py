"""Tests for the Project abstraction."""

from pathlib import Path

from colabdevkit.project.project import Project


def test_project_root(tmp_path):
    project = Project(tmp_path)

    assert isinstance(project.root, Path)
    assert project.root == tmp_path.resolve()


def test_project_name(tmp_path):
    project = Project(tmp_path)

    assert project.name == tmp_path.name


def test_project_exists(tmp_path):
    project = Project(tmp_path)

    assert project.exists() is True


def test_project_nonexistent(tmp_path):
    project_path = tmp_path / "projeto_inexistente"

    project = Project(project_path)

    assert project.exists() is False


def test_project_normalizes_relative_path():
    project = Project(".")

    assert project.root.is_absolute()
