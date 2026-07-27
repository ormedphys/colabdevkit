
from colabdevkit.utils.file_utils import (
    file_exists,
    create_directory,
    directory_exists,
)


def test_file_exists():
    assert file_exists("teste_colabdevkit.txt") is True


def test_create_directory(tmp_path):
    novo_diretorio = tmp_path / "diretorio_teste"

    create_directory(novo_diretorio)

    assert directory_exists(novo_diretorio) is True
