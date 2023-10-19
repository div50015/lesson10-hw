from dataclasses import dataclass
from datetime import datetime, date
from enum import Enum
from datetime import datetime


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    number: str
    date_of_birth: date
    subject: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str


