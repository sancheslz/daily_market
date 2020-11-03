from requester import Requester
from typing import List


class EconomicEvents(Requester):

    paths = {
        'hour': '{0}[{1}]/td[1]/text()',
        'event': '{0}[{1}]/td/a/text()',
        'current': '{0}[{1}]/td[5]/text()',
        'project': '{0}[{1}]/td[6]/text()',
        'previous': '{0}[{1}]/td[7]/span/text()',
    }

    def __init__(self: object) -> None:
        Requester.__init__(self, 'https://br.investing.com/economic-calendar')
        self.tree = self._request()

    def _get_data(self: object, coin: str) -> [List[dict], str]:
        """ Return a list of dictionaries with economic events of day """

        try:
            path = '//table[@id="economicCalendarData"]/tbody/tr'
            items = self.tree.xpath('{}'.format(path))

            for n in range(0, len(items)):
                country = self.tree.xpath('{0}[{1}]/td[2]/text()'.format(
                    path, n))

                country = country[0].strip() if country else None

                if coin == country:

                    data = dict()
                    for key, value in EconomicEvents.paths.items():
                        data[key] = self.tree.xpath(
                            value.format(path, n))[0].strip()

                    yield data

        except:
            print('Problem to get events')

    def events(self: object) -> [List[dict], str]:
        """ Request day events if none, return a message """

        data = list(self._get_data('BRL'))

        if len(data) == 0:
            return 'Sem eventos para hoje'
        return data
