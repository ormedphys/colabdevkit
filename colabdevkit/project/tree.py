"""
Ferramentas para exibição da estrutura de projetos.
"""

from pathlib import Path

from .constants import IGNORED_DIRECTORIES


def print_tree(path: str | Path = ".") -> None:
    """
    Exibe o conteúdo imediato de um diretório.

    Parameters
    ----------
    path : str | Path
        Diretório a ser listado.
    """

    root = Path(path)

    directories = sorted(
        [
            item
            for item in root.iterdir()
            if item.is_dir() and item.name not in IGNORED_DIRECTORIES
        ],
        key=lambda p: p.name.lower(),
    )

    files = sorted(
        [item for item in root.iterdir() if item.is_file()],
        key=lambda p: p.name.lower(),
    )

    for item in directories:
        print(f"📁 {item.name}/")

    for item in files:
        print(f"📄 {item.name}")
