from aoc2021.aocutils import *


class Day01:

    def __init__(self):
        self._day = "01"
        self._isdone = True
        self._nums = read_file_lines_as_num("01")

    @property
    def Day(self):
        return self._day

    @property
    def Done(self):
        return self._isdone

    def solve_1(self):
        cnt = 0
        for i in range(1,len(self._nums)):
            if self._nums[i] > self._nums[i-1]:
                cnt += 1
        return cnt

    def solve_2(self):
        cnt = 0
        for i in range(3, len(self._nums)):
            if self._nums[i] > self._nums[i-3]:
                cnt += 1
        return cnt
