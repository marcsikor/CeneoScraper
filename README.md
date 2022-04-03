# CeneoScraper

# analiza struktury opiniii w serwisie [ceneo.pl](https://www.ceneo.pl/95365253#tab=reviews)

|skladowa | selektor | zmienna | typ |
|---------|----------|---------|-----|
|opinia|div.js_produck-review|review|bs4.element.Tag|
|identyfikator opinii|\[data-entry-id\]|id|str|
|autor|.user-post__autor-name|author|str|
|rekomendacja|.user-post__author-recomendation > em|recommendation|bool|
|liczba gwiazdek|.user-post__score-count|stars|float|
|treść|.user-post__text|content|text|
|data wystawienia|.user-post__published > time:nth-child(1)\[datetime\]|publish_date|str|
|data zalkupu|.user-post__published > time:nth-child(2)\[datetime\]|purchase_date|str|
|dla ilu przydatna|button.vote-yes > span|useful|int|
|dla ilu nieprzydatna|button.vote-no > span|useless|int|
|lista zalet|div.review-feature__item:has\( > div.review-feature__title--positives\)|pros|list|
|lista wad|div.review-feature__item:has\( > div.review-feature__title--negatives\)|cons|list|

## etapy pracy nad projektem

1) Pobranie składowych pojedynczej opipii do niezależnych zmiennych
2) Zapisanie wszysthkich składowych opinii 
3) Coś tam
4) Jeszcze coś
