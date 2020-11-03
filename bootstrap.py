# Library import
import json
# Methods imports
from datetime import datetime
from time import sleep
# Project Imports
from spy import EconomicEvents, Market, Treasure, Newspaper
from twitter import TwitterBot
from models import db_news, db_schedule


def get_dataset():
    with open('./dataset.json') as dataset:
        data = dataset.read()
        return json.loads(data)


def get_news():
    for response in dataset.values():
        status, data = Newspaper(**response).news()

        if status == 200 and len(db_news.get('url == "{}"'.format(
                data.get('href')))) == 0:

            tweet.send_text('@{} - {} - Leia mais em: {}'.format(
                data.get('twitter'),
                data.get('title'),
                data.get('href')
            ))

            db_news.insert(
                data.get('title'),
                datetime.today().strftime('%d/%m/%Y'),
                data.get('href'),
            )


if __name__ == "__main__":

    # Create databases if don't exist
    db_news.create()
    db_schedule.create()
    dataset = get_dataset()
    tweet = TwitterBot()
