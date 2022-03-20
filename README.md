# CeneoScraper

# analiza struktury opiniii w serwisie ceneo.pl

skladowa | selektor | zmienna |
---------|----------|---------|
|opinia|div.js_produck-review|review|
|identyfikator opinii|\[data-entry-id\]|id|
|autor|.user-post__autor-name|author|
|rekomendacja|.user-post__author-recomendation > em|recommendation|
|liczba gwiazdek|.user-post__score-count|stars|
|treść|.user-post__text|content|
|data wystawienia|.user-post__published > time:nth-child(1)\[datetime\]|publish_date|
|data zalkupu|.user-post__published > time:nth-child(2)\[datetime\]|purchase_date|
|dla ilu przydatna|button.vote-yes > span|useful|
|dla ilu nieprzydatna|button.vote-no > span|useless|
|lista zalet|div.review-feature__item:has( > div.review-feature__title--positives)|pros|
|lista wad|div.review-feature__item:has( > div.review-feature__title--negatives)|cons|
