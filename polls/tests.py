from django.test import TestCase
from django_dynamic_fixture import G

from polls.models import Polls


class PollsTest(TestCase):

    def test_search_book_by_author(self):
        book = G(Polls)
        self.assertIsNone(book.name)
