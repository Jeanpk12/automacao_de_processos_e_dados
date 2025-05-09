# API Integration — APIService
Este módulo contém a classe APIService, responsável por realizar a integração com a API JSONPlaceholder, uma API pública utilizada para simulações e testes de aplicações web.

## Classe: APIService
Classe que centraliza chamadas HTTP para obter usuários e posts simulados da API JSONPlaceholder.

### obter_usuarios()
Descrição:
Busca a lista de todos os usuários disponíveis na API.

Parâmetros:
- Nenhum.

Retorno:
- list[dict] – Lista de dicionários, onde cada item representa um usuário (com id, name, email, etc).

Exceções:
- requests.HTTPError – Lançada se a resposta da API indicar erro (ex: status 4xx ou 5xx).

### Exemplo de uso:
```python
api = APIService()
usuarios = api.obter_usuarios()
```
### obter_posts_por_usuario(user_id)
Descrição: Busca todos os posts associados a um usuário específico, com base no seu user_id.

Parâmetros:
- user_id (int) – ID do usuário cujos posts devem ser buscados.

Retorno:
- list[dict] – Lista de dicionários, cada um representando um post (title, body, etc.).

Exceções:
- requests.HTTPError – Lançada caso a requisição falhe.

### Exemplo de uso:

```python
api = APIService()
posts = api.obter_posts_por_usuario(3)
```

## Dependências
Este módulo utiliza:
- **requests** – para envio de requisições HTTP
- **JSONPlaceholder** – API REST de simulação
