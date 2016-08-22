from django.test import TestCase
from django.contrib.auth.models import User


class NewUserTest(TestCase):
    def test_saving_a_POST_request(self):
        self.client.post(
            '/accounts/register/',
            data={'username': 'test',
                  'email': 'test@test.test',
                  'password': 'testtest'}
        )

        self.assertEqual(User.objects.count(), 1)
        user = User.objects.first()
        self.assertEqual(user.username, 'test')


class LoginUserTest(TestCase):
    username = 'test'
    email = 'test@test.test'
    password = 'testtest'

    def setUp(self):
        User.objects.create_user(username=self.username,
                                 email=self.email,
                                 password=self.password)

    def test_login_correct_user(self):
        user = User.objects.first()

        self.client.post(
            '/accounts/login/',
            data={'username': self.username,
                  'password': self.password},
            follow=True
        )

        session = self.client.session

        self.assertEqual(str(user.id), session['_auth_user_id'])

    def test_user_logout(self):
        self.client.get('/accounts/logout/')
        session = self.client.session

        self.assertEqual('', session.get('_auth_user_id', ''))



