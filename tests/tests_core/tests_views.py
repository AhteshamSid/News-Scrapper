import ast

from django.test import TestCase, override_settings, RequestFactory, SimpleTestCase
from django.urls import reverse
from core.views import StatisticsView, HomeView


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestHomeView(SimpleTestCase):

    def test_environment_set_in_context(self) -> None:
        request = RequestFactory().get('/')
        view = HomeView()
        view.setup(request)

    def test_view_urls_exists_at_desired_location(self) -> None:
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self) -> None:
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self) -> None:
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestStatisticsView(TestCase):

    def test_view_urls_exists_at_desired_location(self) -> None:
        response = self.client.get('/statistics/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self) -> None:
        response = self.client.get(reverse('core:statistics'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self) -> None:
        response = self.client.get(reverse('core:statistics'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statistics.html')

    def test_get_all_article_pie_chart_data(self) -> None:
        request = RequestFactory().get('/chart-1/')
        view = StatisticsView()
        view.setup(request)

        json_response = view.get_all_article_pie_chart_data()
        self.assertEqual(json_response.status_code, 200)
        self.assertJSONEqual(json_response.content, {'labels': [],
                                                     'data': [],
                                                     'colors': []})

    def test_get_all_article_tab_chart_data(self) -> None:
        request = RequestFactory().get('/chart-2/')
        view = StatisticsView()
        view.setup(request)

        json_response = view.get_all_article_tab_chart_data()
        self.assertEqual(json_response.status_code, 200)
        self.assertJSONEqual(json_response.content, {'labels': [],
                                                     'data': [],
                                                     'colors': []})

    def test_get_top_en_word_chart_data(self) -> None:
        request = RequestFactory().get('/chart-3/')
        view = StatisticsView()
        view.setup(request)

        json_response = view.get_top_en_word_chart_data()
        data_bytes = json_response.content
        data_dict = data_bytes.decode('UTF-8')
        json_data = ast.literal_eval(data_dict)
        colors = json_data['colors']
        self.assertEqual(json_response.status_code, 200)
        self.assertJSONEqual(json_response.content, {'labels': [],
                                                     'data': [],
                                                     'colors': colors})

    def test_get_top_pl_word_chart_data(self) -> None:
        request = RequestFactory().get('/chart-4/')
        view = StatisticsView()
        view.setup(request)

        json_response = view.get_top_pl_word_chart_data()
        data_bytes = json_response.content
        data_dict = data_bytes.decode('UTF-8')
        json_data = ast.literal_eval(data_dict)
        colors = json_data['colors']
        self.assertEqual(json_response.status_code, 200)
        self.assertJSONEqual(json_response.content, {'labels': [],
                                                     'data': [],
                                                     'colors': colors})


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestBenchmarkView(TestCase):

    def test_view_urls_exists_at_desired_location(self) -> None:
        response = self.client.get('/benchmark/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self) -> None:
        response = self.client.get(reverse('core:benchmark'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self) -> None:
        response = self.client.get(reverse('core:benchmark'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'benchmark.html')

    def test_if_context_has_proper_data(self) -> None:
        response = self.client.get('/benchmark/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['data'][0], tuple)


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestBoardGamesGeekView(TestCase):

    def test_view_urls_exists_at_desired_location(self) -> None:
        response = self.client.get('/bgg/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self) -> None:
        response = self.client.get(reverse('core:bgg'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self) -> None:
        response = self.client.get(reverse('core:bgg'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bgg.html')

    def test_if_context_has_proper_data(self) -> None:
        response = self.client.get('/bgg/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['data'][0], tuple)


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestArcheologyView(TestCase):

    def test_view_urls_exists_at_desired_location(self) -> None:
        response = self.client.get('/archeology/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self) -> None:
        response = self.client.get(reverse('core:archeology'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self) -> None:
        response = self.client.get(reverse('core:archeology'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'archeology.html')

    def test_if_context_has_proper_data(self) -> None:
        response = self.client.get('/archeology/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['data'][0], tuple)


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestToJuzByloView(TestCase):

    def test_view_urls_exists_at_desired_location(self) -> None:
        response = self.client.get('/tojuzbylo/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self) -> None:
        response = self.client.get(reverse('core:tojuzbylo'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self) -> None:
        response = self.client.get(reverse('core:tojuzbylo'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tojuzbylo.html')

    def test_if_context_has_proper_data(self) -> None:
        response = self.client.get('/tojuzbylo/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['data'][0], tuple)


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestComputerWorldView(TestCase):

    def test_view_urls_exists_at_desired_location(self) -> None:
        response = self.client.get('/computerworld/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self) -> None:
        response = self.client.get(reverse('core:computer-world'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self) -> None:
        response = self.client.get(reverse('core:computer-world'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'computer_world_news.html')

    def test_if_context_has_proper_data(self) -> None:
        response = self.client.get('/computerworld/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['data'][0], tuple)


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestPythonView(TestCase):

    def test_view_urls_exists_at_desired_location(self) -> None:
        response = self.client.get('/python/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self) -> None:
        response = self.client.get(reverse('core:python'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self) -> None:
        response = self.client.get(reverse('core:python'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'python.html')

    def test_if_context_has_proper_data(self) -> None:
        response = self.client.get('/python/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['data'][0], tuple)


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestRealPythonView(TestCase):

    def test_view_urls_exists_at_desired_location(self) -> None:
        response = self.client.get('/real-python/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self) -> None:
        response = self.client.get(reverse('core:real-python'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self) -> None:
        response = self.client.get(reverse('core:real-python'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'real_python.html')

    def test_if_context_has_proper_data(self) -> None:
        response = self.client.get('/real-python/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['data'][0], tuple)


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestBushcraftableView(TestCase):

    def test_view_urls_exists_at_desired_location(self) -> None:
        response = self.client.get('/bushcraftable/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self) -> None:
        response = self.client.get(reverse('core:bushcraftable'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self) -> None:
        response = self.client.get(reverse('core:bushcraftable'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bushcraftable.html')

    def test_if_context_has_proper_data(self) -> None:
        response = self.client.get('/bushcraftable/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['data'][0], tuple)
