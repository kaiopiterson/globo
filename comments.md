# Comentários e Decisões

## Escolha da Estrutura

Optei por organizar o código da API em um diretório separado (`api`) para facilitar a manutenção e a escalabilidade da aplicação. Utilizamos Blueprints do Flask para modularizar as rotas.

## Dependências

Utilizei o Flask devido à sua simplicidade e flexibilidade para criar APIs RESTful. Todas as dependências estão listadas no arquivo `requirements.txt`.

## Configurações

Adicionei um arquivo `config.py` (opcional) para gerenciar as configurações da aplicação de forma centralizada. Isso permite uma melhor separação entre código e configuração.
Ainda em teste, caso de tempo.

## Testes

Realizei testes básicos com comandos `curl` para garantir que as rotas da API estão funcionando corretamente.
via postman ou prompt.

# Adicionar comentários
curl -sv http://localhost:5000/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"alice@example.com","comment":"first post!","content_id":1}'
curl -sv http://localhost:5000/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"alice@example.com","comment":"ok, now I am gonna say something more useful","content_id":1}'
curl -sv http://localhost:5000/api/comment/new -X POST -H 'Content-Type: application/json' -d '{"email":"bob@example.com","comment":"I agree","content_id":1}'

# Listar comentários
curl -sv http://localhost:5000/api/comment/list/1

## Melhorias Futuras para dar continuidade ao projeto

- Adicionar autenticação e autorização.
- Implementar persistência de dados usando um banco de dados.
- Melhorar o tratamento de erros e respostas da API.
- Implementar testes unitários e de integração.

