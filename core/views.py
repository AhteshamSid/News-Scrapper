from collections import Counter
from random import randint
import re
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView
from .models import Article, portals, languages
from utils.utils import parse_a_website

QTV_URL = 'https://soundcloud.com/aryqtv/'
NDTV_URL = 'https://www.ndtv.com/entertainment/'
BENCHMARK_URL = 'https://www.benchmark.pl/'
BGG_URL = 'https://boardgamegeek.com/blog/1/boardgamegeek-news'
ZWIAD_HISTORII_URL = 'https://www.zwiadowcahistorii.pl/'
TOJUZBYLO_URL = 'https://tojuzbylo.pl/aktualnosci'
COMPUTER_WORLD_WEB_URL = 'https://www.computerworld.pl/'
PYTHON_WEB_URL = 'https://www.infoworld.com/uk/category/python/'
REAL_PYTHON_WEB_URL = 'https://realpython.com/'
BUSHCRAFTABLE_URL = 'https://bushcraftable.com/'


class HomeView(TemplateView):
    template_name = 'homepage.html'


class StatisticsView(View):
    def get(self, request):
        return render(self.request, 'statistics.html')

    def get_all_article_pie_chart_data(self):
        all_articles = list(Article.objects.all().values_list('portal', flat=True))
        articles = Counter(all_articles)

        colors = []
        for color in range(len(articles)):
            color = '#%06x' % randint(0, 0xFFFFFF)
            colors.append(color)

        context = {
            'labels': list(articles.keys()),
            'data': list(articles.values()),
            'colors': colors,
        }

        return JsonResponse(data=context)

    def get_all_article_tab_chart_data(self):
        all_articles = list(Article.objects.all().values_list('portal', flat=True))
        articles = Counter(all_articles)
        sorted_articles = dict(sorted(articles.items(), key=lambda item: item[1], reverse=True))

        colors = []
        for color in range(len(articles)):
            color = '#%06x' % randint(0, 0xFFFFFF)
            colors.append(color)

        context = {
            'labels': list(sorted_articles.keys()),
            'data': list(sorted_articles.values()),
            'colors': colors,
        }

        return JsonResponse(data=context)

    def get_top_en_word_chart_data(self):
        all_titles = list(Article.objects.filter(language='ENG').values_list('title', flat=True))

        top_words = []
        for title in all_titles:
            split_title = title.split(' ')
            for word in split_title:
                if len(word) > 3:
                    top_words.append(word.lower())

        count_top_words = Counter(top_words)
        sorted_words = dict(sorted(count_top_words.items(), key=lambda item: item[1], reverse=True))

        colors = []
        for color in range(10):
            color = '#%06x' % randint(0, 0xFFFFFF)
            colors.append(color)

        context = {
            'labels': list(sorted_words.keys())[:10],
            'data': list(sorted_words.values())[:10],
            'colors': colors,
        }

        return JsonResponse(data=context)

    def get_top_pl_word_chart_data(self):
        all_titles = list(Article.objects.filter(language='PL').values_list('title', flat=True))

        top_words = []
        for title in all_titles:
            split_title = title.split(' ')
            for word in split_title:
                if len(word) > 3:
                    top_words.append(word.lower())

        count_top_words = Counter(top_words)
        sorted_words = dict(sorted(count_top_words.items(), key=lambda item: item[1], reverse=True))

        colors = []
        for color in range(10):
            color = '#%06x' % randint(0, 0xFFFFFF)
            colors.append(color)

        context = {
            'labels': list(sorted_words.keys())[:10],
            'data': list(sorted_words.values())[:10],
            'colors': colors,
        }

        return JsonResponse(data=context)


class NdtvView(View):
    def get(self, *args, **kwargs):
        soup = parse_a_website(NDTV_URL)

        # Getting data from soup
        data = []
        divs = soup.find_all('div', {'class': 'listItm'})

        for div in divs:
            global img
            url = f"{div.find('a')['href']}"
            title = div.find('a')['title']
            img = parse_a_website(url).find('img', {'id': 'story_image_main'})['src']
            data.append((url, title, img))

        # Creating Article
        Article.check_if_article_already_exist(data, portals[8][1], languages[0][1])

        if len(data) == 0:
            context = {'data': [('#', 'No data to view. Contact with administrator.')]}
            return render(self.request, 'ndtv_news.html', context)

        context = {
            'data': data,
        }
        return render(self.request, 'ndtv_news.html', context, )


class QtvView(View):
    def get(self, *args, **kwargs):
        soup = parse_a_website(QTV_URL)

        # Getting data from soup
        data = []
        divs = soup.find_all('a')
        for div in divs:
            h = div['href']
            i = re.findall('/aryqtv/', h)
            if i and h != "/aryqtv/likes" and h != "/aryqtv/sets" and h != "/aryqtv/comments" and h != "/aryqtv/tracks":
                title = h.replace("/aryqtv/", "").replace("_", " ")
                url = f"https://soundcloud.com{h}"
                # img = div.find('img')['src']
                data.append((url, title))

        # Creating Article
        Article.check_if_article_already_exist(data, portals[9][1], languages[0][1])

        if len(data) == 0:
            context = {'data': [('#', 'No data to view. Contact with administrator.')]}
            return render(self.request, 'qtv.html', context)

        context = {
            'data': data,
        }
        return render(self.request, 'qtv.html', context, )


class BenchmarkView(View):
    def get(self, *args, **kwargs):
        soup = parse_a_website(BENCHMARK_URL)

        # Getting data from soup
        data = []

        sections = soup.find_all('section')
        section_3 = sections[3]
        section_3_divs = section_3.find_all('div')

        for div in section_3_divs[1:2]:
            benchmark_li = div.find_all('li')
            for li in benchmark_li:
                title = (li.find('a').text).split('\t\t\t')[1].split('\n')[0]
                url = f"http://benchmark.pl{li.find('a')['href']}"
                data.append((url, title))

        # Creating Article
        Article.check_if_article_already_exist(data, portals[0][0], languages[1][1])

        # Check if data not empty
        if len(data) == 0:
            context = {'data': [('#', 'No data to view. Contact with administrator.')]}
            return render(self.request, 'benchmark.html', context)

        context = {
            'data': data,
        }
        return render(self.request, 'benchmark.html', context)


class BoardGamesGeekView(View):
    def get(self, *args, **kwargs):
        soup = parse_a_website(BGG_URL)

        # Getting data from soup
        data = []
        posts = soup.find_all("h3", {"class": 'post_title'})

        for post in posts:
            title = post.find('a').text
            url = f"https://boardgamegeek.com{post.find('a')['href']}"
            data.append((url, title))

        # Creating Article
        Article.check_if_article_already_exist(data, portals[1][1], languages[1][1])

        # Check if data not empty
        if len(data) == 0:
            context = {'data': [('#', 'No data to view. Contact with administrator.')]}
            return render(self.request, 'bgg.html', context)

        context = {
            'data': data,
        }
        return render(self.request, 'bgg.html', context, )


class ArcheologyView(View):
    def get(self, *args, **kwargs):
        soup = parse_a_website(ZWIAD_HISTORII_URL)

        # Getting data from soup
        data = []
        divs_1 = soup.find_all("div", {"class": 'td_module_1 td_module_wrap td-animation-stack'})

        for div in divs_1:
            divs_2 = div.find_all('div', {'class': 'td-module-thumb'})
            for element in divs_2:
                title = element.find('a')['title']
                url = element.find('a')['href']
                img = element.find('img')['data-img-url']
                data.append((url, title, img))

        # Creating Article
        Article.check_if_article_already_exist(data, portals[3][1], languages[0][1])

        if len(data) == 0:
            context = {'data': [('#', 'No data to view. Contact with administrator.')]}
            return render(self.request, 'archeology.html', context)

        context = {
            'data': data,
        }
        return render(self.request, 'archeology.html', context)


class ToJuzByloView(View):
    def get(self, *args, **kwargs):
        soup = parse_a_website(TOJUZBYLO_URL)

        # Getting data from soup
        data = []
        tds = soup.find_all('td', {'class': 'col-1 col-first'})

        for td in tds:
            title = (td.find('h2', {'class': 'tytul'}).text).split('\n')[1]
            img = td.find('img')['src']
            href = td.find_all('a')[1]['href']
            url = f"https://tojuzbylo.pl/{href}"
            data.append((url, title, img))

        # Creating Article
        Article.check_if_article_already_exist(data, portals[2][1], languages[0][1])

        if len(data) == 0:
            context = {'data': [('#', 'No data to view. Contact with administrator.')]}
            return render(self.request, 'tojuzbylo.html', context)

        context = {
            'data': data,
        }
        return render(self.request, 'tojuzbylo.html', context, )


class ComputerWorldView(View):
    def get(self, *args, **kwargs):
        soup = parse_a_website(COMPUTER_WORLD_WEB_URL)

        # Getting data from soup
        data = []
        main_div = soup.find('div', {'class': 'left-side'})
        divs = main_div.find_all('div', {'class': 'row-item-icon'})

        for div in divs:
            img = div.find('img', {'class': 'img-fluid'})['src']
            url = f"https://www.computerworld.pl{div.find('a')['href']}"
            title = div.find('a')['href'].split(',')[0].split('/')[2].replace('-', ' ')

            data.append((url, title, img))

        # Creating Article
        Article.check_if_article_already_exist(data, portals[4][1], languages[0][1])

        if len(data) == 0:
            context = {'data': [('#', 'No data to view. Contact with administrator.')]}
            return render(self.request, 'computer_world_news.html', context)

        context = {
            'data': data,
        }
        return render(self.request, 'computer_world_news.html', context, )


class PythonView(View):
    def get(self, *args, **kwargs):
        soup = parse_a_website(PYTHON_WEB_URL)

        # Getting data from soup
        data = []
        divs = soup.find_all('div', {'class': 'post-cont'})
        figs = soup.find_all('figure', {'class': 'well-img'})

        for div, figure in zip(divs, figs):
            title = div.find('a').text
            url = f"https://www.infoworld.com{div.find('a')['href']}"
            img = figure.find('img')['data-original']

            data.append((url, title, img))

        # Creating Article
        Article.check_if_article_already_exist(data, portals[5][1], languages[1][1])

        if len(data) == 0:
            context = {'data': [('#', 'No data to view. Contact with administrator.')]}
            return render(self.request, 'python.html', context)

        context = {
            'data': data,
        }
        return render(self.request, 'python.html', context)


class RealPythonView(View):
    def get(self, *args, **kwargs):
        soup = parse_a_website(REAL_PYTHON_WEB_URL)

        # Getting data from soup
        data = []

        posts = soup.find_all('div', {'class': 'card border-0'})

        for post in posts:
            a_tags = post.find_all('a')[0]
            title = a_tags.find('img')['alt']
            img = a_tags.find('img')['src']
            url = f"https://realpython.com{a_tags['href']}"
            data.append((url, title, img))

        # Creating Article
        Article.check_if_article_already_exist(data, portals[6][1], languages[1][1])

        if len(data) == 0:
            context = {'data': [('#', 'No data to view. Contact with administrator.')]}
            return render(self.request, 'real_python.html', context)

        context = {
            'data': data,
        }
        return render(self.request, 'real_python.html', context)


class BushcraftableView(View):
    def get(self, *args, **kwargs):
        soup = parse_a_website(BUSHCRAFTABLE_URL)

        # Getting data from soup
        data = []

        post_headers = soup.find_all('h2', {'class': 'entry-title'})
        post_images = soup.find_all('div', {'class': 'post-image'})

        for header, image in zip(post_headers, post_images):
            url = header.find('a')['href']
            title = header.find('a').text
            img = image.find('img')['src']
            data.append((url, title, img))

        # Creating Article
        Article.check_if_article_already_exist(data, portals[7][1], languages[1][1])

        if len(data) == 0:
            context = {'data': [('#', 'No data to view. Contact with administrator.')]}
            return render(self.request, 'bushcraftable.html', context)

        context = {
            'data': data,
        }
        return render(self.request, 'bushcraftable.html', context)

# soup.find_all(lambda tag: tag.name == 'p' and 'et' in tag.text)


# https://www.livescience.com/news

# TODO: Widok statystyk. Obliczenie ilości artykułów i piechart na widoku statystycznym,

# TODO: Settingsy porownac do django projektu KWL/Inforshare i pozmieniać.

# detect language - https://pypi.org/project/langdetect/
