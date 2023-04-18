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

print(card1)

print(card1.to_dict())

# ______________________________________
my_dict = {}


def create_dict(string):
    global my_dict
    for index, item in enumerate(string):
        my_dict[index] = item
    return my_dict


print(create_dict('RobPaulWelsh'))
print(my_dict[7])



