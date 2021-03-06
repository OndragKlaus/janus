from typing import Dict

from .contact import Contact
from .util import to_json


class Transaction:
    def __init__(self, id: str, contact, type: str,
                 purpose: str, booking_text: str, amount: float) -> None:
        if isinstance(contact, Dict):
            self.contact = Contact(**contact)
        elif isinstance(contact, Contact):
            self.contact = contact
        else:
            raise Exception('invalid type')

        self.id = id
        self.type = type
        self.purpose = purpose
        self.booking_text = booking_text
        self.amount = amount

    def to_json(self):
        return {
            'id': to_json(self.id),
            'contact': to_json(self.contact),
            'type': to_json(self.type),
            'purpose': to_json(self.purpose),
            'booking_text': to_json(self.booking_text),
            'amount': to_json(self.amount)
        }
