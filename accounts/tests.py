from rest_framework.test import APITransactionTestCase
from rest_framework import status
from accounts.models import User


class AccountsViewsTestCases(APITransactionTestCase):

    def setUp(self):
        # Criação do usuário de teste
        self.obj_user = User.objects.create(id=1, email='tester@take5.com.br', password='tester@take5', full_name='Tester Take5', is_staff=True)

    def tearDown(self):
        self.client.logout()

    def test_accounts(self):
        '''Testa o método GET da view responsável por efetuar a leitura dos dados do usuário'''
        # Given: setUp()
        url = '/accounts/'
        expected_response = [{'id': 1, 'email': 'tester@take5.com.br', 'full_name': 'Tester Take5', 'picture': None}]
        # When:
        response = self.client.get(url)
        body = response.json()
        # Then:
        assert response.status_code == status.HTTP_200_OK
        assert body == expected_response
        assert len(body) == 1
