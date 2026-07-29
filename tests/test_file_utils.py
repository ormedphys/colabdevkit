"""
Tests for file utility functions.
"""

from colabdevkit.utils.file_utils import (
    read_text_file,
    write_text_file,
)


def test_file_exists(tmp_path):
    """
    Verifica se o arquivo é criado.
    """
    arquivo = tmp_path / "teste.txt"

    write_text_file(arquivo, "Olá, mundo!")

    assert arquivo.exists()


def test_read_written_file(tmp_path):
    """
    Verifica se o conteúdo gravado pode ser lido.
    """
    arquivo = tmp_path / "teste.txt"

    write_text_file(arquivo, "Olá, mundo!")

    assert read_text_file(arquivo) == "Olá, mundo!"


def test_overwrite_existing_file(tmp_path):
    """
    Verifica se um arquivo existente é sobrescrito.
    """
    arquivo = tmp_path / "teste.txt"

    write_text_file(arquivo, "Primeira versão")
    write_text_file(arquivo, "Segunda versão")

    assert read_text_file(arquivo) == "Segunda versão"


def test_create_directory(tmp_path):
    """
    Verifica se é possível criar arquivos em diretórios existentes.
    """
    diretorio = tmp_path / "docs"
    diretorio.mkdir()

    arquivo = diretorio / "arquivo.txt"

    write_text_file(arquivo, "Teste")

    assert arquivo.exists()
    assert read_text_file(arquivo) == "Teste"
