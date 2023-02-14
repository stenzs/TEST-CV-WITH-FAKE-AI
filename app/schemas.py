from dataclasses import dataclass
from typing import List


@dataclass
class Stage:
    name: str


@dataclass
class Pipeline:
    name: str
    stages: List[Stage] | dict

    def __post_init__(self):
        self.stages = [Stage(x) for x in self.stages]
