from dataclasses import dataclass


@dataclass
class Person:
    password: int = None
    email: str = None
    first_name: str = None