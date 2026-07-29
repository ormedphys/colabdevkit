from colabdevkit.bootstrap import project_exists


def test_project_exists(tmp_path):
    assert project_exists(tmp_path)