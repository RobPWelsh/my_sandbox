# This is the home_edits branch of sandbox.py
from dataclasses import dataclass
from dataclasses import asdict
import os
import pathlib


@dataclass
class Card:
    summary: str = None
    owner: str = None
    state: str = 'todo'
    id: int = None

    @classmethod
    def from_dict(cls, d):
        return Card(**d)

    def to_dict(self):
        return asdict(self)


my_dict = {'summary': 'do something', 'owner': 'Rob', 'state': 'todo', 'id': 1}
card1 = Card.from_dict(my_dict)
print(card1)  # Card(summary='do something', owner='Rob', state='todo', id=1)
print(card1.to_dict())  # {'summary': 'do something', 'owner': 'Rob', 'state': 'todo', 'id': 1}

card2 = Card('do nothing', 'RW', 'done', 2)
print(card2)  # Card(summary='do nothing', owner='RW', state='done', id=2)
print(card2.to_dict())  # {'summary': 'do nothing', 'owner': 'RW', 'state': 'done', 'id': 2}


# _____________________________________

def test_obj_param(obj):
    return obj.summary


print(test_obj_param(card2))  # do nothing

# ______________________________________
another_dict = {}


def create_dict(string):
    global another_dict
    for index, item in enumerate(string):
        another_dict[index] = item
    return another_dict


print(create_dict('RobPaulWelsh'))  # {0: 'R', 1: 'o', 2: 'b', 3: 'P', 4: 'a', 5: 'u', 6: 'l', 7: 'W', 8: 'e', 9: 'l', 10: 's', 11: 'h'}
print(another_dict[7])  # W
