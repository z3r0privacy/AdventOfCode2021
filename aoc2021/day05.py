from aoc2021.aocutils import *
import re

class Day05:

    def __init__(self):
        self._day = "05"
        self._isdone = False
        self.lines = read_file_lines(self.Day)
        self.rgx = re.compile(r"(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)")

    @property
    def Day(self):
        return self._day

    @property
    def Done(self):
        return self._isdone

    def get_points(self, line):
        match = self.rgx.match(line)
        x1 = int(match.group("x1"))
        x2 = int(match.group("x2"))
        y1 = int(match.group("y1"))
        y2 = int(match.group("y2"))
        return x1, y1, x2, y2

    def solve_1(self):
        lines = [self.get_points(l) for l in self.lines if l]
        coords = {}
        for l in lines:
            if l[0] == l[2]:  # x1 == x2
                start = min(l[1], l[3])
                end = max(l[1], l[3])
                for y in range(start, end+1):
                    k = f"{y},{l[0]}"
                    if k not in coords.keys():
                        coords[k] = 0
                    coords[k] += 1
            elif l[1] == l[3]:  # y1 == y2
                start = min(l[0], l[2])
                end = max(l[0], l[2])
                for x in range(start, end+1):
                    k = f"{l[1]},{x}"
                    if k not in coords.keys():
                        coords[k] = 0
                    coords[k] += 1
        return len([x for x in coords.values() if x >= 2])

    def solve_2(self):
        lines = [self.get_points(l) for l in self.lines if l]
        coords = {}
        for l in lines:
            if l[0] == l[2]:  # x1 == x2
                start = min(l[1], l[3])
                end = max(l[1], l[3])
                for y in range(start, end+1):
                    k = f"{y},{l[0]}"
                    if k not in coords.keys():
                        coords[k] = 0
                    coords[k] += 1
            elif l[1] == l[3]:  # y1 == y2
                start = min(l[0], l[2])
                end = max(l[0], l[2])
                for x in range(start, end+1):
                    k = f"{l[1]},{x}"
                    if k not in coords.keys():
                        coords[k] = 0
                    coords[k] += 1
            else:  # diag
                xmod = 1 if l[0] < l[2] else -1
                x = l[0]
                ymod = 1 if l[1] < l[3] else -1
                y = l[1]
                while x != l[2]+xmod:
                    k = f"{y},{x}"
                    if k not in coords.keys():
                        coords[k] = 0
                    coords[k] += 1
                    x += xmod
                    y += ymod
                    
        return len([x for x in coords.values() if x >= 2])
