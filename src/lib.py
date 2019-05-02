class Name:
    def __init__(self, name, storage=[]):
        self.name = name
        self.storage = storage


class Description(Name):
    def __init__(self, name, description, storage=[]):
        super().__init__(name, storage=storage)
        self.description = description

    def __str__(self):
        return f'{self.name} {self.description}'
