import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'

class APIService:
    """Classe para interagir com a API JSONPlaceholder."""

    def obter_usuarios(self):
        """
        Recupera a lista de usuários da API.

        Returns:
            list: Lista de dicionários, cada um representando um usuário.

        Raises:
            requests.HTTPError: Se a resposta da API indicar erro.
        """
        response = requests.get(f'{BASE_URL}/users')
        response.raise_for_status()
        return response.json()

    def obter_posts_por_usuario(self, user_id):
        """
        Recupera os posts de um usuário específico com base no ID.

        Args:
            user_id (int): ID do usuário cujos posts devem ser buscados.

        Returns:
            list: Lista de dicionários contendo os posts do usuário.

        Raises:
            requests.HTTPError: Se a resposta da API indicar erro.
        """
        response = requests.get(f'{BASE_URL}/posts', params={'userId': user_id})
        response.raise_for_status()
        return response.json()
