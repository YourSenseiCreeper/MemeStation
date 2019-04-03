import datetime

from django.test import TestCase

from .models import Meme


# Test of the buttons and their actions
# Test of the registration system?
# Test of Error404 (Don't have it rn)
# Test of adding an meme and the proper text
# Test of using buttons without permissions?


class MemeTestCase(TestCase):
    def setUp(self):
        Meme.objects.create(description="Przykladowy opis", author="Piotrek",
        image="C:\\Users\\ARKADIUSZ\\PycharmProjects\\MemeStation\\memes\\static\\memes\\pictures\\omfgError404.jpg",
        waiting=True, add_date=datetime.datetime.now(), publication_date=None, likes=None, likes_number=0,
        dislikes=None, dislikes_number=0)

    def test_meme_description(self):
        memik = Meme.objects.get(description="Przykladowy opis")
        self.assertEqual(memik.autor, 'Piotrek')
