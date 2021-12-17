import heapq
from aoc2021.aocutils import *


class Day15:

    def __init__(self):
        self._day = "15"
        self._isdone = True
        self.lines = [[int(c) for c in l if c] for l in read_file_lines(self.Day)]
        self.x_mods = [-1, 0, 1, 0]
        self.y_mods = [0, -1, 0, 1]

    @property
    def Day(self):
        return self._day

    @property
    def Done(self):
        return self._isdone

    def _prepare(self, bigField=False):
        thefield = self.lines
        if bigField:
            self.lines_b = []
            for l in self.lines:
                nl = []
                for i in range(5):
                    for n in l:
                        num = n+i
                        if num > 9:
                            num -= 9
                        nl.append(num)
                self.lines_b.append(nl)
            numlines = len(self.lines_b)
            for i in range(1,5):
                for li in range(numlines):
                    nl = []
                    for n in self.lines_b[li]:
                        num = n+i
                        if num > 9:
                            num -= 9
                        nl.append(num)
                    self.lines_b.append(nl)
            thefield = self.lines_b

        intmax = 2147483647
        dist = {}
        prec = {}
        q = []
        for y in range(len(thefield)):
            for x in range(len(thefield[y])):
                dist[(x,y)] = intmax
                prec[(x,y)] = None
        dist[(0,0)] = 0
        heapq.heappush(q, (0, (0,0)))
        return dist, prec, q

    def _is_in_scope(self, f, x, y):
        if y < 0 or y >= len(f):
            return False
        if x < 0 or x >= len(f[y]):
            return False
        return True

    def solve_1(self):
        dist, prec, q = self._prepare()
        visited = set()
        gy = len(self.lines)-1
        gx = len(self.lines[gy])-1
        while q:
            d, p = heapq.heappop(q)
            visited.add(p)
            if p == (gx, gy):
                break
            for i in range(4):
                _x = p[0]+self.x_mods[i]
                _y = p[1]+self.y_mods[i]
                if self._is_in_scope(self.lines, _x, _y):
                    if (_x, _y) not in visited:
                        newd = d + self.lines[_y][_x]
                        if newd < dist[(_x, _y)]:
                            dist[(_x, _y)] = newd
                            prec[(_x, _y)] = p
                            heapq.heappush(q, (newd, (_x,_y)))
        return dist[(gx,gy)]

        # old version, bellman ford
        dist, prec = self._prepare()
        for i in range(len(dist)-1):
            print(i)
            for y in range(len(self.lines)):
                for x in range(len(self.lines[y])):
                    if dist[(x,y)] is None:
                        continue
                    for m in range(4):
                        _x = x + self.x_mods[m]
                        _y = y + self.y_mods[m]
                        if self._is_in_scope(_x, _y):
                            nd = dist[(x,y)] + self.lines[_y][_x]
                            if dist[(_x, _y)] is None or nd < dist[(_x, _y)]:
                                dist[(_x, _y)] = nd
                                prec[(_x, _y)] = (x,y)
        y = len(self.lines)-1
        x = len(self.lines[y])-1
        return dist[(x,y)]

    def solve_2(self):
        dist, prec, q = self._prepare(bigField=True)
        visited = set() # do not use a list here, this takes very, very, long...
        gy = len(self.lines_b)-1
        gx = len(self.lines_b[gy])-1
        while q:
            d, p = heapq.heappop(q)
            visited.add(p)
            if p == (gx, gy):
                break
            for i in range(4):
                _x = p[0]+self.x_mods[i]
                _y = p[1]+self.y_mods[i]
                if self._is_in_scope(self.lines_b, _x, _y):
                    if (_x, _y) not in visited:
                        newd = d + self.lines_b[_y][_x]
                        if newd < dist[(_x, _y)]:
                            dist[(_x, _y)] = newd
                            prec[(_x, _y)] = p
                            heapq.heappush(q, (newd, (_x,_y)))
        return dist[(gx,gy)]
