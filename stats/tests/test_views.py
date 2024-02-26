from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from checks.models import News


class StatsTest(TestCase):

    def setUp(self):

        self.user = User.objects.create(username='tester', is_staff=True)
        self.user.set_password('1')
        self.user.save()

        self.client = Client()
        self.client.login(username="tester", password="1")

        self.client.post(reverse("index"), {
            "title": "May be fake news title 1",
            "body": "May be fake news body 1"
        })
        self.client.post(reverse("index"), {
            "title": "May be fake news title 2",
            "body": "May be fake news body 2"
        })

    def test_stats(self):
        response = self.client.get(reverse("stats"))
        self.assertEqual(response.status_code, 200)

        news_stats = response.context[0].get("news_stats")
        self.assertEqual(news_stats["all"], 2)

    def test_user_create(self):
        self.client.post(reverse("users-create"), {
            "username": "new_user_1",
            "first_name": "New",
            "last_name": "User",
            "email": "new_user@gmail.com",
            "password": "new_user1pass"
        })

        self.assertEqual(User.objects.count(), 2)

    def test_user_edit(self):
        self.client.post(reverse("users-create"), {
            "username": "new_user_1",
            "first_name": "New",
            "last_name": "User",
            "email": "new_user@gmail.com",
            "password": "new_user1pass"
        })

        new_user = User.objects.last()
        self.client.post(reverse("users-edit", kwargs={"uid": new_user.id}), {
            "username": "new_user_1",
            "first_name": "New",
            "last_name": "User",
            "email": "new_user@gmail.com",
            "middle_name": "New User",
            "subscribed": True,
            "free_checks": 5,
        })
        self.user.refresh_from_db()
        self.assertEqual(new_user.profile.middle_name, "New User")
        self.assertEqual(new_user.profile.subscribed, True)

    def test_user_delete(self):
        self.client.post(reverse("users-create"), {
            "username": "new_user_1",
            "first_name": "New",
            "last_name": "User",
            "email": "new_user@gmail.com",
            "password": "new_user1pass"
        })
        self.assertEqual(User.objects.count(), 2)

        new_user = User.objects.last()
        self.client.post(reverse("users-delete", kwargs={"pk": new_user.pk}))
        self.assertEqual(User.objects.count(), 1)

    def test_check_delete(self):
        self.client.post(reverse("checks-delete", kwargs={"pk": News.objects.last().pk}))
        self.assertEqual(News.objects.count(), 1)
