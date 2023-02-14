import random
from schemas import Image
mock = {"top_left_x": 15, "top_left_y": 20, "w": 100, "h": 200, "conf": 0.8, "label": 1}


class AI:
    def __init__(self, image_string: str):
        self.image_string: str = image_string

    def detect_auto(self):
        if random.choice([True, False]):
            return Image(image_string=self.image_string, **mock)
        return None
