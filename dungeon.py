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


class Generator:
    def __init__(self):
        self.rooms = []

    def generate(self, room, max_depth, depth):
        if depth >= max_depth:
            self.rooms.append(room)
            return
        depth += 1
        rooms = room.split()
        self.generate(rooms[0], max_depth, depth)
        self.generate(rooms[1], max_depth, depth)

    def print(self):
        for room in self.rooms:
            print(str(room))

room = Room(0, 10, 0, 10)
gen = Generator()
gen.generate(room, 3, 0)
gen.print()
