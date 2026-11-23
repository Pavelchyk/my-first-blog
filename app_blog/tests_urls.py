from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView, ArticleList, ArticleCategoryList, ArticleDetail
from .models import Category, Article


class HomeTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(
            category='Innovations',
            slug='innovations'
        )
        Article.objects.create(
            title='Test Article',
            description='Test description',
            slug='test-article',
            category=category
        )

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, HomePageView)

    def test_articles_list_view_status_code(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_articles_list_url_resolves_view(self):
        view = resolve('/articles')
        self.assertEqual(view.func.view_class, ArticleList)

    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=('innovations',))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_category_url_resolves_view(self):
        view = resolve('/articles/category/innovations')
        self.assertEqual(view.func.view_class, ArticleCategoryList)

    def test_article_detail_view_status_code(self):
        article = Article.objects.get(id=1)
        url = article.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_article_detail_url_resolves_view(self):
        article = Article.objects.get(id=1)
        view = resolve(article.get_absolute_url())
        self.assertEqual(view.func.view_class, ArticleDetail)