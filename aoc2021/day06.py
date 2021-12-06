from aoc2021.aocutils import *


class Day06:

    def __init__(self):
        self._day = "06"
        self._isdone = True
        self.initial_fish = [int(s) for s in read_file(self.Day).split(",") if s]

    @property
    def Day(self):
        return self._day

    @property
    def Done(self):
        return self._isdone

    def solve(self, num_days):
        num_fishes = {
            8: 0,
            7: 0,
            6: len([i for i in self.initial_fish if i == 6]),
            5: len([i for i in self.initial_fish if i == 5]),
            4: len([i for i in self.initial_fish if i == 4]),
            3: len([i for i in self.initial_fish if i == 3]),
            2: len([i for i in self.initial_fish if i == 2]),
            1: len([i for i in self.initial_fish if i == 1]),
            0: len([i for i in self.initial_fish if i == 0])
        }

        for _ in range(num_days):
            num_fishes_new = {
                8: num_fishes[0],
                7: num_fishes[8],
                6: num_fishes[7] + num_fishes[0],
                5: num_fishes[6],
                4: num_fishes[5],
                3: num_fishes[4],
                2: num_fishes[3],
                1: num_fishes[2],
                0: num_fishes[1]
            }
            num_fishes = num_fishes_new
        return sum(num_fishes.values())

    def solve_1(self):
        return self.solve(80)

    def solve_2(self):
        return self.solve(256)
