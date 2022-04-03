import requests
import json
from bs4 import BeautifulSoup


url = "https://www.ceneo.pl/95365253#tab=reviews"

all_reviews = []

while url:
    response = requests.get(url)
    
    page_dom = BeautifulSoup(response.text, 'html.parser')
    
    reviews = page_dom.select("div.js_product-review")
    
    for review in reviews:
    
        review_id = review["data-entry-id"]
        author = review.select_one("span.user-post__author-name").text.strip()

        try:

            recommendation = review.select_one('.user-post__author-recomendation > em').text
            recommendation = True if recommendation == "Polecam" else False

        except AttributeError():
            recommendation = None

        stars = review.select_one('.user-post__score-count').text
        stars = float(stars.split('/').pop(0).replace(',','.'))
        content = review.select_one(".user-post__text").text
        publish_date = review.select_one('.user-post__published > time:nth-child(1)')['datetime']
        try:
            purchase_date = review.select_one('.user-post__published > time:nth-child(2)')['datetime']
        except TypeError:
            purchase_date = None
        useful = review.select_one("button.vote-yes > span").text
        useful = int(useful)
        useless = int(review.select_one('button.vote-no > span').text)
        pros = review.select('div.review-feature__item:has( > div.review-feature__title--positives)')
        cons = review.select("div.review-feature__item:has( > div.review-feature__title--negatives)")
    
        pros = [item.text.strip() for item in pros]
        cons = [item.text.strip() for item in cons]
    
        single_review = {
            'review_id': review_id,
            'author': author,
            'recommendation': recommendation,
            'stars': stars,
            'content': content,
            'publish_date': publish_date,
            'purchase_date': purchase_date,
            'useful': useful,
            'useless': useless,
            'pros': pros,
            'cons': cons
        }
    
        all_reviews.append(single_review)
    
    next_page = page_dom.select_one('a.pagination__next')
    try:
        url = "https://www.ceneo.pl/" + next_page["href"]
    except TypeError:
        url = None

with open("./reviews/09365253.json", 'w', encoding='UTF-8') as f:    
    json.dump(all_reviews, f ,indent=4,ensure_ascii=False)