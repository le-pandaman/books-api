from django.test import TestCase
from django.urls import reverse

from .models import Books

# Create your tests here.


class BookTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:

        cls.book = Books.objects.create(
            title='krem',
            author='krem',
            subtitle="krem",
            isbn="111111",
        )

    def test_book_content(self):

        self.assertEqual(self.book.title, 'krem')
        self.assertEqual(self.book.subtitle, 'krem')
        self.assertEqual(self.book.author, 'krem')
        self.assertEqual(self.book.isbn, '111111')

    def test_book_listview(self):

        response = self.client.get(reverse('book_list'))

        self.assertEqual(response.status_code, 200)
