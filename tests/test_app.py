import unittest
from app import app  # Importa a sua aplicação Flask

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Olá, Mundo DevOps com Flask!')

if __name__ == '__main__':
    unittest.main()