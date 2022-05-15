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

## Etapy pracy nad projektem strukturalnym
1. Pobranie elementów pojedynczej opinii do niezależnych zmiennych
2. Zapisanie wszystkich elemntów pojedynczej opinii do jednej zmiennej \(słownik\)
3. Pobranie wszystkich opinii z pojedynczej strony do słowników i dodnie ich do listy
4. Pobranie wszystkich opinii o produkcie z wszystkich stron i zapisanie ich do pliku .json
5. Dodanie możliowści podania id produktu przez użytkownika za pomocą klawiatury
6. Refaktoryzacja \(optymalizacja\) kodu:
    1. utworzenie funkcji do pobierania składowych strony HTML
    2. utworzenie słownika opisującego strukturę opinii wraz z selektorami poszczególnych elementów
    3. zamiana instrukcji pobierających składowe opinii do pojedynczych zmiennych i tworzących z nich słownik na wyrażenie słownikowe \(dictionary comprehension\) tworzące słownik reprezentujący pojedynczą opinię na podstawie słownika selektorów
7. Analiza opinii o wybranym produkcie
    1. wczytanie wszystkich opinii o wskazanym produkcie do obiektu DataFrame
    2. wyliczenie podstawowych statystyk na podstawie opinii
        1. liczba wszystkich opinii o produkcie
        2. liczba opinii w których autor podał listę zalet produktu
        3. liczba opinii w których autor podał listę wad produktu
        4. średnia ocena produktu
    3. przygotowanie wykresów na podstawie zawartości opinii
        1. udział poszczególnych rekomendacji w ogólnej liczbie opinii
        2. histogram częstości występowania poszczególnych ocen (liczby gwiazdek)