class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(self, x, y, char, color, blocked):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.blocked = blocked

    def move(self, dx, dy):
        # Move the entity by a given amount
        self.x += dx
        self.y += dy

    def is_blocked(self, x, y):
        if self.blocked:
            return True

        return False
