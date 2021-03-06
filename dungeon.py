import curses
import random


class Room:
    def __init__(self, left, right, top, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.corridor = None
        self.children = None

    def width(self):
        return self.right - self.left

    def height(self):
        return self.bottom - self.top

    def trim(self, border):
        self.left += border
        self.right -= border
        self.top += border
        self.bottom -= border

    def is_leaf(self):
        if self.children is None:
            return True
        return False

    def split(self):
        # between 1/3 to 2/3 original size
        divisor = random.uniform(1.5, 3)
        h_midpoint = self.left + self.width() / divisor
        v_midpoint = self.top + self.height() / divisor
        room_a = Room(self.left, h_midpoint, self.top, self.bottom)
        room_b = Room(h_midpoint, self.right, self.top, self.bottom)
        self.corridor = (h_midpoint, v_midpoint)
        if self.height() > self.width():
            room_a = Room(self.left, self.right, self.top, v_midpoint)
            room_b = Room(self.left, self.right, v_midpoint, self.bottom)
        self.children = (room_a, room_b)

    def __repr__(self):
        return str(self.left) + "," + str(self.right) + "," + str(self.top) + "," + str(self.bottom)


class Maze:
    def __init__(self, dimension):
        self.dimension = dimension
        self.room = Room(0, self.dimension[0], 0, self.dimension[1])

    def generate(self, max_depth):
        self.recursive_gen(self.room, max_depth, 0)

    def recursive_gen(self, room, max_depth, depth):
        if depth >= max_depth:
            room.trim(1)
            return
        depth += 1
        room.split()
        self.recursive_gen(room.children[0], max_depth, depth)
        self.recursive_gen(room.children[1], max_depth, depth)

    def draw(self):
        self.recursive_draw(self.room)

    def recursive_draw(self, room):
        stdscr = curses.initscr()
        if room.is_leaf():
            for x in range(int(room.left), int(room.right) + 1):
                for y in range(int(room.top), int(room.bottom) + 1):
                    if x == int(room.left) or x == int(room.right):
                        stdscr.addch(y, x, "|")
                    if y == int(room.top) or y == int(room.bottom):
                        stdscr.addch(y, x, "=")
            stdscr.refresh()
            return
        stdscr.addch(int(room.corridor[1]), int(room.corridor[0]), "#")
        self.recursive_draw(room.children[0])
        self.recursive_draw(room.children[1])


maze = Maze([100, 50])
maze.generate(4)
maze.draw()
