import curses
import random


class Room:
    def __init__(self, left, right, top, bottom):
        self.left, self.right, self.top, self.bottom = left, right, top, bottom

    def split(self):
        left, right, top, bottom = self.left, self.right, self.top, self.bottom
        max = 5
        rand = random.randint(2, max + 1)
        direction = random.randint(0, 2)
        if direction < 1:
            room_a = Room(left, (left + right) / rand, top, bottom)
            room_b = Room((left + right) / rand, right, top, bottom)
        else:
            room_a = Room(left, right, top, (top + bottom) / rand)
            room_b = Room(left, right, (top + bottom) / rand, bottom)
        return (room_a, room_b)

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


class Drawer:
    def __init__(self, resolution):
        self.resolution = resolution

    def draw(self, rooms):
        stdscr = curses.initscr()
        for room in rooms:
            r = self.resolution
            for x in range(int(room.left / r), int(room.right / r) - 1):
                for y in range(int(room.bottom / r), int(room.top / r) - 1):
                    stdscr.addch(y, x, "#")
        stdscr.refresh()


room = Room(0, 30, 10, 0)
gen = Generator()
gen.generate(room, 3, 0)
dr = Drawer(0.25)
dr.draw(gen.rooms)
