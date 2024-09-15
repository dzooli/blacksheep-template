from _collections_abc import dict_items
from dataclasses import dataclass


@dataclass
class Scope:
    def __init__(self, items: dict_items):
        for k, v in items:
            setattr(self, k, str(v))
