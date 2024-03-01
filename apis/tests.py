from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from books.models import Books
# Create your tests here.


class APITests(APITestCase):

    @classmethod
    def setUpTestData(cls):

        cls.book = Books.objects.create(
            title='krem',
            subtitle='krem',
            author='krem',
            isbn='1111111',
        )

    def test_api_listview(self):

        response = self.client.get(reverse('book_list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Books.objects.count(), 1)
        self.assertContains(response, self.book)
