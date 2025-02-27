import unittest
import app  # Importa o módulo app.py (nossa aplicação Flask)

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client() # Cria um cliente de teste do Flask
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/') # Faz uma requisição GET para a rota '/'
        self.assertEqual(response.status_code, 200) # Verifica se o status code é 200 (OK)
        self.assertEqual(response.data.decode('utf-8'), "Olá Mundo Flask com Testes!") # Verifica se o conteúdo da resposta é o esperado

if __name__ == '__main__':
    unittest.main()
