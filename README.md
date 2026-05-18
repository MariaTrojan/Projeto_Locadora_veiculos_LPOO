## Projeto_Locadora_veiculos_LPOO 


Este é o projeto base utilizado na disciplina de Linguagem de Programação Orientada a Objetos (LPOO) do curso de Ciência da Computação, semestre 2026-1, ministrada pela Professora Vanessa.

O objetivo deste projeto é servir como base prática para a aplicação de conceitos de Orientação a Objetos e Padrões de Projeto (Design Patterns) estudados em sala de aula.



## Funcionalidades Implementadas 
Foi desenvolvida a funcionalidade de gestão de locações de veículos, contemplando duas visões distintas do sistema: Administrador e Usuário da Locadora, seguindo o padrão MVC com persistência em banco de dados.

## Área do Administrador    
Foi criada uma tela exclusiva para o administrador, onde é possível ter controle total sobre as locações, permitindo:

- Criar novas locações com qualquer configuração (datas e status)
- Editar locações existentes
- Visualizar detalhes completos
- Remover locações do sistema

Essa área permite ajustes mais livres, sendo utilizada para gerenciamento e correção de dados.


## Área do Usuário   
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

## Detalhamento de Aprendizado

- **Dificuldades Encontradas:**  
Durante o desenvolvimento, tive dificuldades em entender exatamente quais etapas deveriam ser realizadas em alguns momentos do projeto. Em muitos casos, me baseei nos arquivos já existentes e no conteúdo apresentado em aula, porém nem sempre ficava claro qual seria o próximo passo a seguir.  
Além disso, por se tratar de um projeto com muitos arquivos e camadas (Model, View, Controller e DAO), senti dificuldade em localizar onde deveriam ser feitas determinadas alterações, o que acabou tornando o processo mais confuso.  
Também enfrentei problemas na identificação de erros, pois ao modificar uma parte do código, frequentemente surgiam falhas em outros pontos do sistema, dificultando ainda mais.
  
- **Como resolvi:**  
Para superar essas dificuldades, utilizei como base os materiais disponibilizados em aula, além de realizar pesquisas externas para complementar o entendimento. Também contei com o auxílio de ferramentas de Inteligência Artificial, principalmente nos momentos em que encontrava dificuldades para identificar erros ou quando não estava claro qual deveria ser o próximo passo no desenvolvimento.


- **Principal Aprendizado:**
Os principais aprendizados foram a melhor compreensão de como funciona a integração com o banco de dados, especialmente nas operações de CRUD. Também consegui entender melhor como as partes do sistema são interligadas e o funcionamento das camadas Controller, DAO e View.


## Declaração de Uso de IA
- [ ] **Nenhuma IA foi utilizada** na elaboração deste código.
- [x] **Utilizei IA** como ferramenta de apoio.

- **Ferramenta(s):** ChatGPT
- **Finalidade:**  
Como mencionei anteriormente, utilizei esse recurso principalmente nos momentos em que me perdia sobre como prosseguir no desenvolvimento. Também recorri a ele em situações em que não entendia exatamente como implementar alguma parte, pedindo explicações passo a passo para conseguir desenvolver enquanto aprendia.  
Além disso, nos momentos em que ficava travada, busquei ajuda para identificar o que estava faltando ou o que eu estava fazendo de forma incorreta, o que contribuiu para a continuidade do projeto.


- **Validação:** Declaro que todo o código gerado foi lido, testado e compreendido.
