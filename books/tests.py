from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Book,Auther
from django.urls import reverse

# Create your tests here.
class BookTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='aboud', email='aboud@gmail.com', password='aboud1234'
        )

        self.auther = Auther.objects.create(
            name='Dario', age=40, nationality='american'
        )

        self.book = Book.objects.create(
            title='python', auther = self.auther, category = 'computer',isbn = 125, description = 'good book', employee = self.user)

    def test_model_representation(self):
        self.assertEqual(str(self.book),'python')

    def test_model_content(self):
        self.assertEqual(self.book.title,'python')
        self.assertEqual(str(self.book.auther),'Dario')
        self.assertEqual(self.book.isbn,125)

    