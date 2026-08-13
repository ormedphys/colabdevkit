# ADR-0002 — Descoberta de Pacotes Python

## Status

Aceito

## Contexto

O ColabDevKit é estruturado como uma biblioteca Python composta
por um pacote principal e diversos subpacotes.

Durante a Sprint 0005, os testes automatizados não conseguiram
importar o pacote `colabdevkit` porque o projeto não estava
instalado no ambiente Python utilizado pelo pytest.

A configuração inicial do `pyproject.toml` declarava apenas o
pacote raiz:

```toml
[tool.setuptools]
packages = ["colabdevkit"]
```

Essa configuração não representava adequadamente a estrutura
modular existente no projeto.

## Decisão

O projeto utilizará o mecanismo de descoberta automática de
pacotes do setuptools.

A configuração será:

```toml
[tool.setuptools.packages.find]
include = ["colabdevkit*"]
```

Dessa forma, o pacote principal e seus subpacotes serão
descobertos automaticamente durante o processo de construção
e instalação.

Durante o desenvolvimento, o projeto será instalado em modo
editável utilizando:

```text
python -m pip install -e .
```

## Consequências

O ColabDevKit poderá ser instalado como um pacote Python
completo, mantendo a estrutura modular existente.

Novos subpacotes adicionados posteriormente dentro de
`colabdevkit` serão descobertos automaticamente, sem necessidade
de atualizar manualmente uma lista de pacotes no
`pyproject.toml`.

O modo editável permite que alterações no código-fonte sejam
refletidas diretamente no ambiente de desenvolvimento sem a
necessidade de reinstalar o pacote após cada modificação.

Essa configuração também permite que a suíte de testes seja
executada utilizando o pacote instalado, reproduzindo de forma
mais adequada o comportamento de uma biblioteca Python real.
