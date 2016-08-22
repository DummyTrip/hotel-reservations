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
