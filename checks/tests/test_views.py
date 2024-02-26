from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from checks.models import *
from django.contrib.auth.models import User

from checks.views import ChecksArchive


class CheckTest(TestCase):

    def setUp(self):

        self.user = User.objects.create(username='tester')
        self.user.set_password('1')
        self.user.save()

        self.client = Client()
        self.client.login(username="tester", password="1")

    def test_check_news(self):
        response = self.client.post(reverse("index"), {
            "title": "May be fake news title",
            "body": "May be fake news body"
        })
        self.user.profile.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(News.objects.count(), 1)
        self.assertEqual(self.user.profile.free_checks, 4)

    def test_archive(self):
        self.client.post(reverse("index"), {
            "title": "May be fake news title 1",
            "body": "May be fake news body 1"
        })
        self.client.post(reverse("index"), {
            "title": "May be fake news title 2",
            "body": "May be fake news body 2"
        })

        response = self.client.get(reverse("archive"))
        news = response.context_data["objects"]

        self.assertQuerysetEqual(news, News.objects.all().filter(user=self.user).order_by("created"))