def calcular_media_caracteres(posts):
    """
    Calcula a média de caracteres no campo 'body' de uma lista de posts.

    Parâmetros:
        posts (list): Lista de dicionários, onde cada dicionário representa um post com a chave 'body'.

    Retorna:
        float: Média arredondada para 2 casas decimais do número de caracteres nos 'body' dos posts.
               Retorna 0 se a lista estiver vazia.
    """
    if not posts:
        return 0
    total = sum(len(post['body']) for post in posts)
    return round(total / len(posts), 2)
