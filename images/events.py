from . import ImageGen
from typing import List


class EventsImg(ImageGen):

    def render(self: object, data: List[dict]) -> int:

        titles = position = {
            'Hora': 35,
            'Evento': 120,
            'Atual': 700,
            'Projeção': 800,
            'Anterior': 900
        }

        for key, value in position.items():
            self.content.text(
                (value, 130),
                key,
                font=self.style.get('h2'),
                fill=self.style.get('fontcolor')
            )

        position = {
            'hour': 35,
            'event': 120,
            'current': 700,
            'project': 800,
            'previous': 900
        }

        y = 170
        for item in range(0, len(data)):
            for key, value in position.items():
                self.content.text(
                    (value, y),
                    data[item].get(key) or '-',
                    font=self.style.get('h2'),
                    fill=self.style.get('fontcolor')
                )
            y += 40

        self.board.save('./assets/events.png', format="png")
        return 200
