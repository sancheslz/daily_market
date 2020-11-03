# Library import
import json
# Methods imports
from datetime import datetime
from time import sleep
# Project Imports
from spy import EconomicEvents, Market, Treasure, Newspaper
from twitter import TwitterBot
from images import TreasureImg, MarketImg, EventsImg
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
    if len(db_schedule.get(
        'date == "{}" AND category == "TD"'.format(
            datetime.today().strftime('%d/%m/%Y')))) == 0:

        status, treasure = Treasure().buy()
        if status == 200:
            image = TreasureImg()
            image.add_title(
                100, 'Confira os preços e taxas de hoje no tesouro direto')
            img_status = image.render(treasure)

        if img_status == 200:
            tweet.send_media(
                './assets/treasure.png',
                'Confira as taxas do Tesouro Direto'
            )

            db_schedule.insert(
                datetime.today().strftime('%d/%m/%Y'),
                'TD',
            )


def gen_market_img():
    if len(db_schedule.get(
        'date == "{}" AND category == "MKT"'.format(
            datetime.today().strftime('%d/%m/%Y')))) == 0:

        gainers_status, gainers_data = Market().gainers()
        losers_status, losers_data = Market().losers()

        if gainers_status == 200 and losers_status == 200:
            img = MarketImg()
            img.add_title(330, 'Fechamento do Mercado')
            img_status = img.render({
                'gainers': gainers_data,
                'losers': losers_data
            })

        if img_status == 200:
            tweet.send_media(
                './assets/market.png',
                'Confira o Fechamento do Mercado'
            )

            db_schedule.insert(
                datetime.today().strftime('%d/%m/%Y'),
                'MKT',
            )


def get_events_img():
    if len(db_schedule.get(
        'date == "{}" AND category == "EE"'.format(
            datetime.today().strftime('%d/%m/%Y')))) == 0:

        status, events = EconomicEvents().events()
        if status == 200:
            image = EventsImg()
            image.add_title(350, 'Eventos Econômicos')
            img_status = image.render(events)

            if img_status == 200:
                tweet.send_media(
                    './assets/events.png',
                    'Confira os Eventos Econômicos de Hoje'
                )

            db_schedule.insert(
                datetime.today().strftime('%d/%m/%Y'),
                'EE',
            )

        elif status == 201:
            tweet.send_text('Nenhum evento econômico previsto para hoje')

            db_schedule.insert(
                datetime.today().strftime('%d/%m/%Y'),
                'EE',
            )


def economics():
    if len(db_schedule.get(
        'date == "{}" AND category == "ED"'.format(
            datetime.today().strftime('%d/%m/%Y')))) == 0:

        status, economics = Market().economics()
        if status == 200:
            tweet.send_text(
                'Confira os Indicadores do Mercado\n'+'\n'.join([
                    f"{item.get('item')} > {item.get('value')} ({item.get('percent')})"
                    for item in economics]
                ))

        db_schedule.insert(
            datetime.today().strftime('%d/%m/%Y'),
            'ED',
        )


if __name__ == "__main__":

    # Create databases if it doesn't exist
    db_news.create()
    db_schedule.create()
    dataset = get_dataset()
    tweet = TwitterBot()
