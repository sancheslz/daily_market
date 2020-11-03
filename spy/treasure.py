from .requester import Requester
from typing import List


class Treasure(Requester):

    """ Get Information from National Treasure 

    Usage Example:
            treasure = Treasure()
            treasure.buy()

    Output Example:
            [
                {
                    'title': 'Tesouro Selic 2025',
                    'due': '2025-03-01T00:00:00',
                    'unit': 106.41,
                    'price': 10641.17,
                    'tax': 0.188
                }
            ]
    """

    def __init__(self: object) -> None:
        """ Request date from National Treasure """

        url = 'https://www.tesourodireto.com.br/json/br/com/b3/tesourodireto/service/api/treasurybondsinfo.json'
        Requester.__init__(self, url)
        self.tree = self._request(json=True)

    def _get_data(self: object) -> List[dict]:
        """ Return a list with all available offers """

        for item in self.tree['response']['TrsrBdTradgList']:
            data = item['TrsrBd']
            if data['minInvstmtAmt'] != 0 and data['semiAnulIntrstInd'] == False:

                yield {
                    'title': data['nm'],
                    'due': data['mtrtyDt'],
                    'unit': data['minInvstmtAmt'],
                    'price': data['untrInvstmtVal'],
                    'tax': data['anulInvstmtRate'],
                }

    def buy(self: object) -> List[dict]:
        """ Return buy offers """
        return list(self._get_data())
