from dataclasses import dataclass

@dataclass
class User:
    name = str
    email = str
    current_address = str
    permanent_address = str

    # def __init__(self):
    #     self.name = name
    #     self.email = email
    #     self.current_address = current_address
    #     self.permanent_address = permanent_address


