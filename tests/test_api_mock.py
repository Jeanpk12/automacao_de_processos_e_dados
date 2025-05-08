import unittest
from unittest.mock import patch
from services.api import APIService

class TestAPIService(unittest.TestCase):
    @patch('services.api.requests.get')
    def test_obter_usuarios(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'id': 1, 'name': 'Usuário Teste'}]
        api = APIService()
        usuarios = api.obter_usuarios()
        self.assertEqual(len(usuarios), 1)
        self.assertEqual(usuarios[0]['name'], 'Usuário Teste')

    @patch('services.api.requests.get')
    def test_obter_posts_por_usuario(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'userId': 1, 'body': 'Post de teste'}]
        api = APIService()
        posts = api.obter_posts_por_usuario(1)
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0]['body'], 'Post de teste')

if __name__ == '__main__':
    unittest.main()
