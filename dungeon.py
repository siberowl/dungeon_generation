class Room:
    def __init__(self, left, right, top, bottom):
        self.left, self.right, self.top, self.bottom = left, right, top, bottom

    def split(self):
        left, right, top, bottom = self.left, self.right, self.top, self.bottom
        room_left = Room(left, (left + right) / 2, top, bottom)
        room_right = Room((left + right) / 2, right, top, bottom)
        return (room_left, room_right)

    def __repr__(self):
        return (
            str(self.left)
            + ","
            + str(self.right)
            + ","
            + str(self.top)
            + ","
            + str(self.bottom)
        )

