
from colabdevkit.utils.file_utils import file_exists


def test_file_exists():
    assert file_exists("teste_colabdevkit.txt") is True
