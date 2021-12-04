from aoc2021.aocutils import *

class Board:
    def __init__(self, rows) -> None:
        self.nums = []
        self.marked = []
        for rr in rows:
            r = []
            m = []
            for n in [_n for _n in rr.split(" ") if _n]:
                r.append(int(n))
                m.append(False)
            self.nums.append(r)
            self.marked.append(m)
    
    def cross_num(self, num):
        for y in range(5):
            for x in range(5):
                if self.nums[y][x] == num:
                    self.marked[y][x] = True
    
    def has_won(self):
        if any(all(mrow) for mrow in self.marked):
            return True
        for x in range(5):
            res = True
            for y in range(5):
                if not self.marked[y][x]:
                    res = False
                    break
            if res:
                return True
        return False

    def get_sum(self):
        s = 0
        for y in range(5):
            for x in range(5):
                if not self.marked[y][x]:
                    s += self.nums[y][x]
        return s

class Day04:

    def __init__(self):
        self._day = "04"
        self._isdone = True
        self.lines = read_file_lines(self.Day)

    @property
    def Day(self):
        return self._day

    @property
    def Done(self):
        return self._isdone

    def solve_1(self):
        nums = [int(i) for i in self.lines[0].split(",")]
        boards = []
        l = 2
        while l < len(self.lines):
            boards.append(Board(self.lines[l:l+5]))
            l += 6
        
        for n in nums:
            for b in boards:
                b.cross_num(n)
                if b.has_won():
                    return b.get_sum()*n
        
        return -1


    def solve_2(self):
        nums = [int(i) for i in self.lines[0].split(",")]
        boards = []
        l = 2
        while l < len(self.lines):
            boards.append(Board(self.lines[l:l+5]))
            l += 6
        
        for n in nums:
            toremove = []
            for b in boards:
                b.cross_num(n)
                if b.has_won():
                    if len(boards) == 1:
                        return b.get_sum()*n
                    else:
                        toremove.append(b)
            for b in toremove:
                boards.remove(b)
        
        return -1