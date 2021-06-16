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

    def test_book_list_view(self):
        url = reverse('book_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'python')
        self.assertTemplateUsed(response,'books/book_list.html')

    def test_book_detail_view(self):
        url = reverse('book_detail',args=['1'])
        response = self.client.get(url)
        no_response = self.client.get('/2/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'computer')
        self.assertTemplateUsed(response,'books/book_detail.html')

    def test_book_ceate_view(self):
        url = reverse('book_create')
        response_get = self.client.get(url)
        response_post = self.client.post(
            url,
            {
                'title':'calculus',
                'auther' : self.auther, 
                'category' : 'math',
                'isbn' : 365, 
                'description' : 'nice math book', 
                'employee' : self.user
            },
            follow=True
            )
        self.assertEqual(response_get.status_code,200)
        self.assertTemplateUsed(response_get,'books/book_create.html')

    def test_book_update_view(self):
        url = reverse('book_update',args='1')
        response_get = self.client.get(url)
        response = self.client.post(
            url,
            {
                'title':'calculus',
                'auther' : self.auther, 
                'category' : 'math',
                'isbn' : 365, 
                'description' : 'nice math book', 
                'employee' : self.user
            },
        )
        redirct_url = reverse('book_detail',args='1')
        self.assertEqual(response_get.status_code,200)
        self.assertTemplateUsed(response_get,'books/book_update.html')

    def test_book_delete_view(self):
        url = reverse('book_delete',args='1')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'books/book_delete.html')

    