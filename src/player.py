# Write a class to hold player information, e.g. what room they are in
# currently.
from lib import Name


class Player(Name):
    def __init__(self, name, current_room, storage=[]):
        super().__init__(name, storage=storage)
        self.current_room = current_room

    def move_player(self, new_room):
        self.current_room = new_room

    def get_item(self, item):
        self.storage.append(item)

    def drop_item(self, item):
        self.storage.remove(item)
