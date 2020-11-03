from PIL import ImageFont, Image, ImageDraw
from typing import List


class ImageGen:

    def __init__(self: object) -> None:
        self.style = {
            'fontcolor': (41, 51, 115),
            'h1': ImageFont.truetype('Verdana', 25),
            'h2': ImageFont.truetype('Verdana', 20)
        }

        self.draw_board()

    def draw_board(self: object) -> None:
        self.board = Image.new('RGBA', (1024, 512), color=(255, 255, 255))
        self.content = ImageDraw.Draw(self.board)
        self.content.rectangle([(22, 115), (1000, 107)], fill=(41, 51, 115))

    def add_title(self: object, start: int, text: str) -> None:  # start == 100
        self.content.text(
            (start, 44),
            text.upper(),
            font=self.style.get('h1'),
            fill=self.style.get('fontcolor')
        )

    def render(self: object, data: List[dict]) -> int:
        pass
