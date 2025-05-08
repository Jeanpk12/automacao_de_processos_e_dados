import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'

class APIService:
    def obter_usuarios(self):
        response = requests.get(f'{BASE_URL}/users')
        response.raise_for_status()
        return response.json()

    def obter_posts_por_usuario(self, user_id):
        response = requests.get(f'{BASE_URL}/posts', params={'userId': user_id})
        response.raise_for_status()
        return response.json()
