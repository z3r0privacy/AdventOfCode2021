from aoc2021.aocutils import *

class Day07:

    def __init__(self):
        self._day = "07"
        self._isdone = True
        self.init_positions = [int(i) for i in read_file(self.Day).split(",") if i]

    @property
    def Day(self):
        return self._day

    @property
    def Done(self):
        return self._isdone

    def solve_1(self):
        start = min(self.init_positions)
        end = max(self.init_positions)
        min_fuel = None
        for c in range(start,end+1):
            fuel = 0
            for p in self.init_positions:
                fuel += abs(p-c)
            if not min_fuel or fuel < min_fuel:
                min_fuel = fuel
        return min_fuel
            

    def solve_2(self):
        start = min(self.init_positions)
        end = max(self.init_positions)
        min_fuel = None
        for c in range(start,end+1):
            fuel = 0
            for p in self.init_positions:
                n = abs(p-c)
                fuel += int((n*(n+1))/2)
            if not min_fuel or fuel < min_fuel:
                min_fuel = fuel
        return min_fuel
