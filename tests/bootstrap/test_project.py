
"""
Tests for bootstrap.project.
"""

from colabdevkit.bootstrap import project_exists


def test_project_exists(tmp_path):
    """
    Verifica que um diretório existente é reconhecido.
    """
    assert project_exists(tmp_path)
