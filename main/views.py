from django.shortcuts import render
from .models import Citie, Category, News_Article


def index(request):
	novotroitsk_news = News_Article.objects.filter(citie = 1)[:15]
	orsk_news = News_Article.objects.filter(citie = 2)[:15]
	guy_news = News_Article.objects.filter(citie = 3)[:15]
	return render(request, 'main/index.html', {'novotroitsk_news': novotroitsk_news, 'orsk_news': orsk_news, 'guy_news': guy_news})


def article(request, article_id):
	a = News_Article.objects.get(id = article_id)
	return render(request, 'main/article.html', {'news_article': a})


def category(request, category_name):
	a = Category.objects.get(name = category_name)
	novotroitsk_news = News_Article.objects.filter(citie = 1, category = a.id)[:15]
	orsk_news = News_Article.objects.filter(citie = 2, category = a.id)[:15]
	guy_news = News_Article.objects.filter(citie = 3, category = a.id)[:15]
	return render(request, 'main/category.html', {'category': a, 'novotroitsk_news': novotroitsk_news, 'orsk_news': orsk_news, 'guy_news': guy_news})