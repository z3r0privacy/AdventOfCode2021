from aoc2021.aocutils import *
import math

class Day03:

    def __init__(self):
        self._day = "03"
        self._isdone = True
        self.lines = read_file_lines(self.Day)

    @property
    def Day(self):
        return self._day

    @property
    def Done(self):
        return self._isdone

    def solve_1(self):
        size = len(self.lines[0])
        absMax = math.floor(len(self.lines)/2) + 1
        gamma = ""
        epsilon = ""
        for i in range(size):
            cnt1 = 0
            for b in self.lines:
                if b[i] == "1":
                    cnt1 += 1
            if cnt1 >= absMax:
                gamma += "1"
                epsilon += "0"
            else:
                gamma += "0"
                epsilon += "1"
        gammav = int(gamma, base=2)
        epsilonv = int(epsilon, base=2)
        return gammav*epsilonv

    def solve_2(self):
        def filter(lines, keepExpr):
            pos = 0
            while len(lines) > 1:
                cnt0 = 0
                cnt1 = 0
                for l in lines:
                    if l[pos] == "0":
                        cnt0 += 1
                    else:
                        cnt1 += 1
                keep = keepExpr(cnt0, cnt1)
                _nlines = []
                for l in lines:
                    if l[pos] == keep:
                        _nlines.append(l)
                pos += 1
                lines = _nlines
            return lines[0]

        oxyline = filter(self.lines, lambda c0, c1: "1" if c1 >= c0 else "0")
        co2line = filter(self.lines, lambda c0, c1: "0" if c0 <= c1 else "1")

        return int(oxyline, base=2) * int(co2line, base=2)
