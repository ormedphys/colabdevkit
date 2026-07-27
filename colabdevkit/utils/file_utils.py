"""
Utilitários para operações com arquivos.
"""

from pathlib import Path

def _to_path(
    path: str | Path,
) -> Path:
    """
    Converte a entrada para Path.
    """
    return Path(path)


def write_text_file(
    path: str | Path,
    content: str,
    encoding: str = "utf-8",
) -> None:
    """
    Cria ou sobrescreve um arquivo texto.
    """
    Path(path).write_text(content, encoding=encoding)


def read_text_file(
    path: str | Path,
    encoding: str = "utf-8",
) -> str:
    """
    Lê um arquivo texto.
    """
    return Path(path).read_text(encoding=encoding)


def file_exists(
    path: str | Path,
) -> bool:
    """
    Verifica se um arquivo existe.
    """
    return _to_path(path).is_file()


def directory_exists(
    path: str | Path,
) -> bool:
    """
    Verifica se um diretório existe.
    """
    return Path(path).is_dir()


def delete_file(
    path: str | Path,
)   -> None:
    """
    Remove um arquivo.

    Parameters
    ----------
    path : str | Path
        Caminho do arquivo.
    """
    Path(path).unlink()


def delete_directory(
    path: str | Path,
)   -> None:
    """
    Remove um diretório.

    Parameters
    ----------
    path : str | Path
        Caminho do diretório.
    """
    Path(path).rmdir()


def create_directory(
    path: str | Path,
) -> None:
    """
    Cria um diretório.

    Parameters
    ----------
    path : str | Path
        Caminho do diretório.
    """
    Path(path).mkdir(
        parents=True,
        exist_ok=True,
    )


def list_files(
    path: str | Path,
) -> list[Path]:
    """
    Lista os arquivos de um diretório.

    Parameters
    ----------
    path : str | Path
        Diretório a ser listado.

    Returns
    -------
    list[Path]
        Lista de arquivos.
    """
    return sorted(
        [
            item
            for item in Path(path).iterdir()
            if item.is_file()
        ],
        key=lambda p: p.name.lower(),
    )
