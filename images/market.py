from . import ImageGen
from typing import List


class MarketImg(ImageGen):

    def render(self: object, data: List[dict]) -> int:

        self.content.text(
            (160, 140),
            'Maiores Altas',
            font=self.style.get('h2'),
            fill=self.style.get('fontcolor')
        )

        self.content.text(
            (670, 140),
            'Maiores Baixas',
            font=self.style.get('h2'),
            fill=self.style.get('fontcolor')
        )

        position = {
            'gainers': [
                [(35, 200), (305, 200), (405, 200)],
                [(35, 260), (305, 260), (405, 260)],
                [(35, 320), (305, 320), (405, 320)],
                [(35, 380), (305, 380), (405, 380)],
                [(35, 440), (305, 440), (405, 440)],
            ],

            'losers': [
                [(531, 200), (801, 200), (905, 200)],
                [(531, 260), (801, 260), (905, 260)],
                [(531, 320), (801, 320), (905, 320)],
                [(531, 380), (801, 380), (905, 380)],
                [(531, 440), (801, 440), (905, 440)],
            ],
        }

        for key in position.keys():
            for pos in range(0, len(position.get(key))):
                self.content.text(
                    position.get(key)[pos][0],
                    str(data[key][pos].get('company')),
                    font=self.style.get('h2'),
                    fill=self.style.get('fontcolor')
                )

                self.content.text(
                    position.get(key)[pos][1],
                    str(data[key][pos].get('value')),
                    font=self.style.get('h2'),
                    fill=self.style.get('fontcolor')
                )

                self.content.text(
                    position.get(key)[pos][2],
                    str(data[key][pos].get('percent')),
                    font=self.style.get('h2'),
                    fill=self.style.get('fontcolor')
                )

        self.board.save('./assets/market.png', format="png")
        return 200
