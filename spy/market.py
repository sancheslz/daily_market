from requester import Requester
from typing import List


class Market(Requester):
    """ ...

    Usage Example:
            market = Market()
            market.gainers()

    Output Example:
            [
                {
                    'company': 'IRB Brasil ON',
                    'value': '6,77',
                    'var': '+0,63',
                    'percent': '+10,26%'
                }
            ]
    """

    paths = {
        'market': {
            'company': '/td/a/text()',
            'value': '/td[3]/text()',
            'var': '/td[4]/text()',
            'percent': '/td[5]/text()',
        },

        'economics': {
            'item': '{0}[{1}]/div/a/text()',
            'value': '{0}[{1}]/div/div/div/text()',
            'percent': '{0}[{1}]/div/div/span/text()',
        }
    }

    def __init__(self: object) -> None:
        Requester.__init__(self, 'https://br.investing.com/markets/brazil')
        self.tree = self._request()

    def _get_market_data(self: object, key: str) -> List[dict]:

        try:
            path = self.tree.xpath('//table[@id="{}"]/tbody/tr'.format(key))

            for n in range(1, len(path)+1):

                info = dict()
                data_path = '//table[@id="{0}"]/tbody/tr[{1}]'.format(key, n)
                for field, path in Market.paths['market'].items():
                    info[field] = self.tree.xpath(data_path+path)[0]

                yield info

        except:
            print('Problem loading {} data'.format(key))

    def gainers(self):
        return list(self._get_market_data('markets_gainers'))

    def losers(self):
        return list(self._get_market_data('markets_losers'))

    def _get_economics(self: object) -> List[dict]:
        try:

            source = '//div[@id="markets"]/div'
            for n in range(1, len(self.tree.xpath(source))):

                data = dict()
                for field, path in Market.paths['economics'].items():
                    info = self.tree.xpath(path.format(source, n))
                    data[field] = info[1] if field == 'percent' else info[0]
                yield data

        except:
            return 'Erro ao carregar os indicadores econômicos'

    def economics(self: object) -> List[dict]:
        return list(self._get_economics())
