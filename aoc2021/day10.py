from aoc2021.aocutils import *
from collections import deque

class Day10:

    def __init__(self):
        self._day = "10"
        self._isdone = True
        self.lines = read_file_lines(self.Day)
        self.pairs = {
            '<': '>',
            '(': ')',
            '[': ']',
            '{': '}'
        }

    @property
    def Day(self):
        return self._day

    @property
    def Done(self):
        return self._isdone

    def solve_1(self):
        c_values = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
        }
        sum = 0
        for line in self.lines:
            stack = deque()
            for c in line:
                if c in ['(', '[', '{', '<']:
                    stack.append(c)
                else:
                    start = stack.pop()
                    if self.pairs[start] != c:
                        sum += c_values[c]
                        break
        return sum

    def solve_2(self):
        c_values = {
            ')': 1,
            ']': 2,
            '}': 3,
            '>': 4
        }
        sums = []
        for line in self.lines:
            illegal = False
            stack = deque()
            for c in line:
                if c in ['(', '[', '{', '<']:
                    stack.append(c)
                else:
                    start = stack.pop()
                    if self.pairs[start] != c:
                        illegal = True
                        break
            if not illegal:
                sum = 0
                while len(stack) > 0:
                    o = stack.pop()
                    c = self.pairs[o]
                    sum *= 5
                    sum += c_values[c]
                sums.append(sum)
        
        sums.sort()
        return sums[int(len(sums)/2)]
