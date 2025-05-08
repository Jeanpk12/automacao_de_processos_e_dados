import unittest
from utils.helpers import calcular_media_caracteres

class TestHelpers(unittest.TestCase):
    def test_media_caracteres_com_posts(self):
        posts = [
            {'body': 'texto 1'},
            {'body': 'mais texto aqui'}
        ]
        resultado = calcular_media_caracteres(posts)
        self.assertEqual(resultado, round((len('texto 1') + len('mais texto aqui')) / 2, 2))

    def test_media_caracteres_sem_posts(self):
        resultado = calcular_media_caracteres([])
        self.assertEqual(resultado, 0)

if __name__ == '__main__':
    unittest.main()
