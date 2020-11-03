from urllib.request import Request, urlopen
import ssl
from lxml import html
from json import loads


class Requester:
    """ Responsible to request pages from a url and return the page structure
    """
    
    # Default Header used to request data
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    def __init__(self: object, url: str) -> None:
        self.url = url

    def _request(self: object, *, json=False: bool) -> dict:
        """ Request the url page and if works return the HTML element """
        try:
            request = Request(self.url, headers=Requester.headers,)
            context = ssl.SSLContext()
            web_byte = urlopen(request, context=context).read()
            webpage = web_byte.decode('utf-8')
            if json:
                return loads(webpage)
            tree = html.fromstring(webpage)
            return tree
        except:
            print('Bad request')
