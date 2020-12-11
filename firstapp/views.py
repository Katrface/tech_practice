from django.shortcuts import render, redirect

from .forms import ArticleCardForm
from .models import ArticleCard
from .services.card_article_services import get_head_cards, get_cards

import folium


def main(request):
    context = {'card_list': get_head_cards(6)}
    return render(request, 'firstapp/main.html', context)


def news(request):
    search_query = request.GET.get('search', '')
    context = {'card_list': get_cards(search_query),
               'search_query': search_query}
    return render(request, 'firstapp/news.html', context)


def news_create(request):
    form = ArticleCardForm()
    if request.method == 'POST':
        form = ArticleCardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/news', permanent=True)
    context = {'form': form}
    return render(request, 'firstapp/newsCreate.html', context)


def news_detail(request, pk):
    card = ArticleCard.objects.get(pk=pk)
    form = ArticleCardForm(instance=card)
    if request.method == "POST":
        _news_update(request, card)
        return redirect('/news', permanent=True)
    context = {'form': form,
               'id': card.pk}
    return render(request, 'firstapp/newsDetail.html', context)


def _news_update(request, card):
    form = ArticleCardForm(request.POST, instance=card)
    if form.is_valid():
        form.save()
        return redirect('/news')


def news_delete(request, pk):
    card = ArticleCard.objects.get(pk=pk)
    card.delete()
    return redirect('/news')

