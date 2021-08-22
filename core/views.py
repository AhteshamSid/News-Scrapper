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
        all_titles = list(Article.objects().values_list('title', flat=True))

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
        Article.check_if_article_already_exist(data, portals[0][1])

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
        Article.check_if_article_already_exist(data, portals[1][1])

        if len(data) == 0:
            context = {'data': [('#', 'No data to view. Contact with administrator.')]}
            return render(self.request, 'qtv.html', context)

        context = {
            'data': data,
        }
        return render(self.request, 'qtv.html', context, )


