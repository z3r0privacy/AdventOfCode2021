from aoc2021.aocutils import *
from queue import Queue
import math


class Day09:

    def __init__(self):
        self._day = "09"
        self._isdone = True
        self.heights = [[int(n) for n in l if n] for l in read_file_lines(self.Day) if l]

    @property
    def Day(self):
        return self._day

    @property
    def Done(self):
        return self._isdone

    def get_num(self, x, y):
        if y < 0 or y >= len(self.heights):
            return 10
        if x < 0 or x >= len(self.heights[y]):
            return 10
        return self.heights[y][x]

    def solve_1(self):
        sum = 0
        for y in range(len(self.heights)):
            for x in range(len(self.heights[y])):
                curr = self.get_num(x, y)
                left = self.get_num(x-1, y)
                top = self.get_num(x, y-1)
                right = self.get_num(x+1, y)
                down = self.get_num(x, y+1)
                if curr < left and curr < top and curr < right and curr < down:
                    sum += 1 + curr
        return sum

    def solve_2(self):
        lowpoints = []
        for y in range(len(self.heights)):
            for x in range(len(self.heights[y])):
                curr = self.get_num(x, y)
                left = self.get_num(x-1, y)
                top = self.get_num(x, y-1)
                right = self.get_num(x+1, y)
                down = self.get_num(x, y+1)
                if curr < left and curr < top and curr < right and curr < down:
                    lowpoints.append((x,y))
        basins = []
        for lp in lowpoints:
            toaddpoints = Queue()
            addedpoints = set()
            toaddpoints.put(lp)
            addedpoints.add(lp)
            while not toaddpoints.empty():
                cp = toaddpoints.get()
                x = cp[0]
                y = cp[1]
                curr = self.get_num(x, y)
                left = self.get_num(x-1, y)
                top = self.get_num(x, y-1)
                right = self.get_num(x+1, y)
                down = self.get_num(x, y+1)
                if left < 9 and left > curr and (x-1,y) not in addedpoints:
                    addedpoints.add((x-1, y))
                    toaddpoints.put((x-1, y))
                if right < 9 and right > curr and (x+1,y) not in addedpoints:
                    addedpoints.add((x+1, y))
                    toaddpoints.put((x+1, y))
                if top < 9 and top > curr and (x,y-1) not in addedpoints:
                    addedpoints.add((x, y-1))
                    toaddpoints.put((x, y-1))
                if down < 9 and down > curr and (x, y+1) not in addedpoints:
                    addedpoints.add((x, y+1))
                    toaddpoints.put((x, y+1))
            basins.append(len(addedpoints))

        basins.sort(reverse=True)
        return math.prod(basins[0:3])
