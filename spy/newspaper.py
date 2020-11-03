from .requester import Requester


class Newspaper(Requester):
    """Get the economic breaking news from the passed newspaper

    Usage Example:
            paper = Newspaper(**estadao)
            paper.news()

    Output Example:
            {
                    'source': 'Estadão Economia',
                    'title': ' Gatilho para conter despesa com pessoal abre espaço de R$ 40 bi no Orçamento ',
                    'href': 'https://economia.estadao.com.br/noticias/geral,gatilho-para-conter-despesa-com-pessoal-abre-espaco-de-r-40-bi-no-orcamento,70003404312',
                    'quote': 'Estudo mostra que medidas previstas no teto de gastos teriam potencial equivalente a 0,5 p.p. do PIB'
            }

    """

    def __init__(self: object, **kwargs: dict) -> None:
        """ Receive a dictionary from newspaper_set.py """

        Requester.__init__(self, kwargs.get('url'))

        self.user = kwargs.get('user')
        self.instagram = kwargs.get('instagram')
        self.twitter = kwargs.get('twitter')
        self.title_path = kwargs.get('title_path')
        self.href_path = kwargs.get('href_path')
        self.quote_path = kwargs.get('quote_path') or False
        self.link_correction = kwargs.get('link_correction') or False

    def news(self: object) -> dict:
        """ Collect data from the website """

        data = dict()
        try:
            tree = self._request()
            data['source'] = self.user.upper()
            data['title'] = tree.xpath(self.title_path)[0]
            data['href'] = tree.xpath(self.href_path)[0]
            if self.link_correction:
                data['href'] = self.link_correction + data['href']
            if self.quote_path:
                data['quote'] = tree.xpath(self.quote_path)[0]

            return data

        except:
            print('Problem with news from {}'.format(self.user))
