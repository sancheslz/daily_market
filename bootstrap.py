# Library import
import json
# Methods imports
from datetime import datetime
from time import sleep
# Project Imports
from spy import EconomicEvents, Market, Treasure, Newspaper
from twitter import TwitterBot
from images import TreasureImg
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


def gen_treasure_img():
    status, treasure = Treasure().buy()
    if status == 200:
        print('generating image...')
        image = TreasureImg()
        image.add_title(
            100, 'Confira os preços e taxas de hoje no tesouro direto')
        img_status = image.render(treasure)

    if img_status == 200 and len(db_schedule.get('date == "{}"'.format(datetime.today().strftime('%d/%m/%Y')))) == 0:
        tweet.send_media(
            './assets/treasure.png',
            'Confira as taxas do Tesouro Direto'
        )

        db_schedule.insert(
            datetime.today().strftime('%d/%m/%Y'),
            'TD',
        )


if __name__ == "__main__":

    # Create databases if don't exist
    db_news.create()
    db_schedule.create()
    dataset = get_dataset()
    tweet = TwitterBot()
