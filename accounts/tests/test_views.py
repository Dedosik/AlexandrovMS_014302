from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class AccountsTest(TestCase):

    def setUp(self):

        self.user = User.objects.create(username='tester')
        self.user.set_password('1')
        self.user.save()

        self.client = Client()
        self.client.login(username="tester", password="1")

    def test_subscribe(self):
        response = self.client.post(reverse("subscribe"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), "Подписка оформлена!")

        self.user.profile.refresh_from_db()
        self.assertEqual(self.user.profile.subscribed, True)
