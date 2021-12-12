from aoc2021.aocutils import *


class Day12:

    def __init__(self):
        self._day = "12"
        self._isdone = True
        self.connections = read_file_lines(self.Day)
        self.map = None

    @property
    def Day(self):
        return self._day

    @property
    def Done(self):
        return self._isdone

    def _build_map(self):
        self.map = {}
        for c in self.connections:
            l = c.split("-")[0]
            r = c.split("-")[1]
            if l not in self.map.keys():
                self.map[l] = []
            if r not in self.map.keys():
                self.map[r] = []
            if r not in self.map[l]:
                self.map[l].append(r)
            if l not in self.map[r]:
                self.map[r].append(l)

    def _is_upper(self, s):
        return all(ord(c) in range(ord('A'), ord('Z')+1) for c in s)

    def _get_num_ways1(self, p, way):
        if p == "end":
            return 1
        num_ways = 0
        for cons in self.map[p]:
            if cons not in way:
                is_upper = self._is_upper(cons)
                if not is_upper:
                    way.append(cons)
                num_ways += self._get_num_ways1(cons, way)
                if not is_upper:
                    way.pop()
        return num_ways

    def _get_num_ways2(self, p, way, has_double):
        if p == "end":
            return 1
        num_ways = 0
        for cons in self.map[p]:
            if cons not in way:
                is_upper = self._is_upper(cons)
                if not is_upper:
                    way.append(cons)
                num_ways += self._get_num_ways2(cons, way, has_double)
                if not is_upper:
                    way.pop()
            elif cons != 'start' and not has_double:
                way.append(cons)
                num_ways += self._get_num_ways2(cons, way, True)
                way.pop()

        return num_ways


    def solve_1(self):
        self._build_map()
        num_ways = self._get_num_ways1('start', ['start'])
        return num_ways

    def solve_2(self):
        self._build_map()
        num_ways = self._get_num_ways2('start', ['start'], False)
        return num_ways
