from django.urls import path
from .views import  HomeView, StatisticsView, NdtvView, QtvView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('ndtv/', NdtvView.as_view(), name="ndtv"),
    path('qtv/', QtvView.as_view(), name="qtv"),

    path('chart-1/', StatisticsView.get_all_article_pie_chart_data, name='chart-1'),
    path('chart-2/', StatisticsView.get_all_article_tab_chart_data, name='chart-2'),
    path('chart-3/', StatisticsView.get_top_en_word_chart_data, name='chart-3'),
    path('chart-4/', StatisticsView.get_top_pl_word_chart_data, name='chart-4'),

    ]
