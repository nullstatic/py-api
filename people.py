# people.py

from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

PEOPLE = {
    "One": {
        "fname": "One",
        "lname": "Zero",
        "timestamp": get_timestamp(),
    },
    "Two": {
        "fname": "Two",
        "lname": "Zero",
        "timestamp": get_timestamp(),
    },
    "Three": {
        "fname": "Three",
        "lname": "Zero",
        "timestamp": get_timestamp(),
    },
}

def read_all():
    return list(PEOPLE.values())