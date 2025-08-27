from django.test import TestCase
from django.test import Client

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'nome teste',
            'email': 'teste@teste.com',
            'assunto': 'Meu assunto',
            'mensagem': 'Minha Mensagem'
        }

        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEqual(request.status_code, 302)