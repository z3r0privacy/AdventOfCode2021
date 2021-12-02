from aoc2021.aocutils import *


class Day02:

    def __init__(self):
        self._day = "02"
        self._isdone = True
        self._instrs = read_file_lines(self.Day)

    @property
    def Day(self):
        return self._day

    @property
    def Done(self):
        return self._isdone

    def solve_1(self):
        depth = 0
        hpos = 0
        for i in self._instrs:
            iparts = i.split(" ")
            dir = iparts[0]
            num = int(iparts[1])

            if dir == "up":
                depth -= num
            elif dir == "down":
                depth += num
            elif dir == "forward":
                hpos += num
            else:
                raise Exception("Illegal direction! " + dir)
        return depth*hpos

    def solve_2(self):
        depth = 0
        hpos = 0
        aim = 0

        for i in self._instrs:
            iparts = i.split(" ")
            dir = iparts[0]
            num = int(iparts[1])

            if dir == "up":
                aim -= num
            elif dir == "down":
                aim += num
            elif dir == "forward":
                hpos += num
                depth += num*aim
            else:
                raise Exception("Illegal direction! " + dir)
        return depth*hpos
