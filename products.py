from typing import float


class Product:
    def __init__(self,
                 name: str,
                 price : float,
                 description=''):
        self.name = name
        self.price = price
        self.description = description


    def display(self):
        print(f'Naziv: {self.name}')



