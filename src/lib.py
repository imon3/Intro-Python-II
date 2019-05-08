class Name:
    def __init__(self, name, storage=[]):
        self.name = name
        self.storage = storage

    def add_item(self, item):
        self.storage = item

    def __str__(self):
        return f'Name: {self.name} Storage: {self.storage}'


class Description(Name):
    def __init__(self, name, description, storage=[]):
        super().__init__(name, storage=storage)
        self.description = description

    def __str__(self):
        return f'Name: {self.name}\n Description: {self.description}\n Storage: {self.storage}'

    def __repr__(self):
        return f'Name:{self.name} Description:{self.description}'
