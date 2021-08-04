from django.test import TestCase
from core.models import Article
from django.utils import timezone


class TestArticleModel(TestCase):

    def create_article(
            self,
            title='Test Title',
            language='X',
            portal='TestPortal.com',
            date_created=timezone.now(),
            url='https://www.test.com'):

        return Article.objects.create(
            portal=portal, title=title,
            language=language,
            url=url,
            date_created=date_created)

    def test_article_creation(self):
        article = self.create_article()
        self.assertIsInstance(article, Article)
        self.assertEqual(article.__str__(), f'{article.portal} - {article.title}')
