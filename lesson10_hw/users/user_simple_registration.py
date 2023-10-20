from dataclasses import dataclass


@dataclass
class User:
    name: str
    email: str
    current_address: str
    permanent_address: str
