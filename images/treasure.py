from . import ImageGen
from typing import List


class TreasureImg(ImageGen):

    def render(self: object, data: List[dict]) -> int:
        position = [
            {
                'title': (60, 200),
                'due': (380, 200),
                'unit': (560, 200),
                'price': (700, 200),
                'tax': (850, 200)
            },
            {
                'title': (60, 250),
                'due': (380, 250),
                'unit': (560, 250),
                'price': (700, 250),
                'tax': (850, 250)
            },
            {
                'title': (60, 300),
                'due': (380, 300),
                'unit': (560, 300),
                'price': (700, 300),
                'tax': (850, 300)
            },
            {
                'title': (60, 350),
                'due': (380, 350),
                'unit': (560, 350),
                'price': (700, 350),
                'tax': (850, 350)
            },
            {
                'title': (60, 400),
                'due': (380, 400),
                'unit': (560, 400),
                'price': (700, 400),
                'tax': (850, 400)
            },
            {
                'title': (60, 450),
                'due': (380, 450),
                'unit': (560, 450),
                'price': (700, 450),
                'tax': (850, 450)
            },
        ]

        titles = {
            'Título': (60, 150),
            'Vencimento': (380, 150),
            'Preço Unit.': (560, 150),
            'Valor Total': (700, 150),
            'Taxa': (850, 150)
        }

        for title, value in titles.items():
            self.content.text(
                value,
                title,
                font=self.style.get('h2'),
                fill=self.style.get('fontcolor')
            )

        for item in range(0, len(data)):
            for key, value in data[item].items():
                self.content.text(
                    position[item][key],
                    str(value),
                    font=self.style.get('h2'),
                    fill=self.style.get('fontcolor')
                )

        self.board.save('./assets/treasure.png', format="png")
        return 200
