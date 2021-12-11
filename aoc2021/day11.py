from sys import flags
from aoc2021.aocutils import *
from collections import deque


class Day11:

    def __init__(self):
        self._day = "11"
        self._isdone = True
        self.curr_state = [[int(n) for n in l] for l in read_file_lines(self.Day)]
        self.surroundpos = [(-1,0), (-1,1), (0,1), (1,1), (1, 0), (1,-1), (0, -1), (-1, -1)]

    @property
    def Day(self):
        return self._day

    @property
    def Done(self):
        return self._isdone

    def _get_state(self, x, y):
        if y < 0 or y >= len(self.curr_state):
            return None
        if x < 0 or x >= len(self.curr_state[y]):
            return None
        return self.curr_state[y][x]

    def _perform_step(self):
        flashes = 0
        flashqueue = deque()
        for y in range(len(self.curr_state)):
            for x in range(len(self.curr_state[y])):
                self.curr_state[y][x] += 1
                if self.curr_state[y][x] == 10:
                    flashqueue.append((x,y))
        while len(flashqueue) > 0:
            currflash = flashqueue.pop()
            flashes += 1
            for p in self.surroundpos:
                _x = currflash[0]+p[0]
                _y = currflash[1]+p[1]
                s = self._get_state(_x, _y)
                if s is not None and s != 10:
                    s += 1
                    self.curr_state[_y][_x] = s
                    if s == 10:
                        flashqueue.append((_x,_y))
        for y in range(len(self.curr_state)):
            for x in range(len(self.curr_state[y])):
                if self.curr_state[y][x] == 10:
                    self.curr_state[y][x] = 0
        return flashes

    def solve_1(self):
        flashes = 0
        for _ in range(100):
            flashes += self._perform_step()
        return flashes

    def solve_2(self):
        currstep = 100
        while True:
            self._perform_step()
            currstep += 1
            if all(all(n == 0 for n in l) for l in self.curr_state):
                return currstep
