# ADR-0003 — Abstração `Project`

## Status

Aceito

## Contexto

O ColabDevKit possui diversos módulos destinados a diferentes
responsabilidades, incluindo bootstrap, GitHub, Google Drive,
testing, documentation, automation e release.

Para que esses módulos possam evoluir de forma independente, é
necessário estabelecer uma representação comum do projeto sobre o
qual essas ferramentas irão operar.

As Sprints anteriores estabeleceram funções básicas para localizar
e manipular o diretório do projeto, incluindo `project_exists`,
`project_root` e `change_directory`.

Essas funções fornecem operações sobre o filesystem, mas ainda não
definem uma abstração central que represente um projeto ColabDevKit.

## Decisão

O ColabDevKit adotará `Project` como a abstração central para
representar um projeto no filesystem.

A responsabilidade principal de `Project` será fornecer acesso
estruturado às informações fundamentais do projeto, incluindo:

- identidade;
- localização;
- configuração;
- estrutura;
- estado de existência.

A abstração deverá permanecer pequena e coesa, evitando concentrar
responsabilidades que pertencem a outros componentes do sistema.

Operações especializadas permanecerão em módulos próprios.

Entre elas:

- operações Git;
- integração com GitHub;
- operações Google Drive;
- execução de testes;
- geração de documentação;
- automação;
- gerenciamento de releases.

O `Project` deverá servir como uma entidade sobre a qual esses
componentes poderão operar, e não como responsável pela execução
dessas operações.

## Consequências

A adoção de `Project` estabelece uma abstração comum para os
diferentes componentes do ColabDevKit.

Isso reduz o acoplamento entre os módulos e evita que cada componente
implemente sua própria representação ou descoberta do diretório do
projeto.

A abstração poderá evoluir incrementalmente conforme novas
necessidades forem identificadas.

A implementação inicial deverá permanecer simples, evitando a
criação prematura de uma classe excessivamente complexa ou de um
"God Object".

As funções de bootstrap existentes continuarão sendo utilizadas
quando apropriado e poderão ser integradas progressivamente à nova
abstração.

## Escopo futuro

A implementação inicial de `Project` poderá fornecer informações
como:

- nome do projeto;
- caminho raiz;
- existência;
- configuração;
- estrutura do projeto.

Detalhes da API e das responsabilidades específicas serão definidos
durante a implementação e os testes da Sprint 0006.
