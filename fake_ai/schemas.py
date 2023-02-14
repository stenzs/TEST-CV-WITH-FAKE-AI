from dataclasses import dataclass
from pydantic import BaseModel


class PostImage(BaseModel):
    image_string: str


@dataclass
class Image:
    image_string: str
    top_left_x: int
    top_left_y: int
    w: int
    h: int
    conf: float
    label: int
