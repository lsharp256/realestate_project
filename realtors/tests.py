from django.test import TestCase
from django.urls import reverse


class LogInTest(TestCase):

    def test_registration_success(self):
        credentials = {
            'username': 'testuser',
            'email': 'testuser@mail.com',
            'first_name': 'first',
            'last_name': 'last',
            'password': 'secret',
            'confirm_password': 'secret',
        }

        response = self.client.post(reverse('signup'), credentials)
        assert response.status_code == 302

    def test_registration_incorrect_pass(self):
        credentials = {
            'username': 'testuser',
            'email': 'testuser@mail.com',
            'first_name': 'first',
            'last_name': 'last',
            'password': 'secret',
            'confirm_password': 'notsecret',
        }

        response = self.client.post(reverse('signup'), credentials)
        assert response.status_code == 200
        assert 'Password does not match.' in str(response.content)

    def test_registration_incomplete(self):
        credentials = {
            'username': 'dfhtjyr',
            'first_name': 'first',
            'last_name': 'last',
            'password': 'secret',
            'confirm_password': 'secret',
        }

        response = self.client.post(reverse('signup'), credentials)
        assert response.status_code == 200
        assert 'id_email' in str(response.content)