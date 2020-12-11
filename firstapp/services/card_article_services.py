from firstapp.models import HeadArticleCard, ArticleCard


def get_head_cards(count):
    head_card_list = HeadArticleCard.objects.all()[:count]
    card_list = []
    for card in head_card_list:
        card_list.append(card.article_card)
    return card_list


def get_cards(search_query):
    cards = ArticleCard.objects.all()
    if search_query:
        cards = cards.filter(title__icontains=search_query)
    return cards
