**Projeto_Locadora_veiculos_LPOO** 


Este é o projeto base utilizado na disciplina de Linguagem de Programação Orientada a Objetos (LPOO) do curso de Ciência da Computação, semestre 2026-1, ministrada pela Professora Vanessa.

O objetivo deste projeto é servir como base prática para a aplicação de conceitos de Orientação a Objetos e Padrões de Projeto (Design Patterns) estudados em sala de aula.



**Funcionalidades Implementadas**  
Foi desenvolvida a funcionalidade de gestão de locações de veículos, contemplando duas visões distintas do sistema: Administrador e Usuário da Locadora, seguindo o padrão MVC com persistência em banco de dados.

**Área do Administrador**  
Foi criada uma tela exclusiva para o administrador, onde é possível ter controle total sobre as locações, permitindo:

- Criar novas locações com qualquer configuração (datas e status)
- Editar locações existentes
- Visualizar detalhes completos
- Remover locações do sistema

Essa área permite ajustes mais livres, sendo utilizada para gerenciamento e correção de dados.


**Área do Usuário**  
Foi implementada uma interface voltada ao usuário da locadora, onde é possível:

Criar uma nova reserva, informando:
- Data de início e fim
- Categoria do veículo (econômico, executivo, luxo)
- Visualizar apenas os veículos disponíveis no período selecionado  


Realizar as seguintes ações:
- Locar (retirar o veículo)
- Devolver (finalizar a locação)
- Cancelar a reserva
- Ver detalhes da locação
