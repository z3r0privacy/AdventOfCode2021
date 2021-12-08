from typing import Tuple
from aoc2021.aocutils import *

class Day08:

    def __init__(self):
        self._day = "08"
        self._isdone = True
        self.lines = read_file_lines(self.Day)
        self.digits = {
            0: ['a','b','c','e','f','g'],
            1: ['c','f'],
            2: ['a','c','d','e','g'],
            3: ['a','c','d','f','g'],
            4: ['b','c','d','f'],
            5: ['a','b','d','f','g'],
            6: ['a','b','d','e','f','g'],
            7: ['a','c','f'],
            8: ['a','b','c','d','e','f','g'],
            9: ['a','b','c','d','f','g']
        }

    @property
    def Day(self):
        return self._day

    @property
    def Done(self):
        return self._isdone

    def _possible_locs(self, numdigits):
        locs = []
        for v in self.digits.values():
            if len(v) == numdigits:
                locs.extend(v)
        return list(set(locs))

    def solve_1(self):
        c = 0
        for l in self.lines:
            o = l.split(" | ")[1].split(" ")
            for n in o:
                if len(n) in [2,3,4,7]:
                    c += 1
        return c


    def map_digits_to_num(self, mapping, segments):
        l = [mapping[s] for s in segments]
        for d, segs in self.digits.items():
            if len(segs) == len(l):
                match = True
                for s in segs:
                    if s not in l:
                        match = False
                        break
                if match:
                    return d
        return None

    def _ver_bt(self, a_map, ver_inputs):
        for input in ver_inputs:
            num = self.map_digits_to_num(a_map, input)
            if num is None:
                return False
        return True

    def _bt(self, mappings, a_map, c_s, ver_inputs):
        if ord(c_s) > ord('g'):
            sol_map = {}
            for k,v in a_map.items():
                sol_map[v] = k
            if self._ver_bt(sol_map, ver_inputs):
                return sol_map
            return None

        used_vals = a_map.values()
        for k, v in mappings.items():
            if k not in used_vals and c_s in v:
                a_map[c_s] = k
                sol_map = self._bt(mappings, a_map, chr(ord(c_s)+1), ver_inputs)
                if sol_map:
                    return sol_map
                else:
                    a_map[c_s] = None
        return None

    def solve_2(self):
        sum = 0
        for l in self.lines:
            mapping = {
                'a': ['a','b','c','d','e','f','g'],
                'b': ['a','b','c','d','e','f','g'],
                'c': ['a','b','c','d','e','f','g'],
                'd': ['a','b','c','d','e','f','g'],
                'e': ['a','b','c','d','e','f','g'],
                'f': ['a','b','c','d','e','f','g'],
                'g': ['a','b','c','d','e','f','g']
            }
            inputs = l.split(" | ")[0].split(" ")
            outputs = l.split(" | ")[1].split(" ")
            verify = inputs+outputs

            for k in mapping.keys():
                for i in inputs:
                    if k not in i:
                        continue
                    plocs = self._possible_locs(len(i))
                    for s in ['a','b','c','d','e','f','g']:
                        if s in mapping[k] and s not in plocs:
                            mapping[k].remove(s)
            
            res_map = self._bt(mapping, {}, 'a', verify)
            if not res_map:
                raise Exception("No valid mapping found...")

            odigit = 0
            for o in outputs:
                odigit *= 10
                odigit += self.map_digits_to_num(res_map, o)
            sum += odigit
        return sum
            


    def _nope(self):
        for l in self.lines:
            mapping = {
                'a': ['a','b','c','d','e','f','g'],
                'b': ['a','b','c','d','e','f','g'],
                'c': ['a','b','c','d','e','f','g'],
                'd': ['a','b','c','d','e','f','g'],
                'e': ['a','b','c','d','e','f','g'],
                'f': ['a','b','c','d','e','f','g'],
                'g': ['a','b','c','d','e','f','g']
            }
            inputs = l.split(" | ")[0].split(" ")
            unmapped = ['a','b','c','d','e','f','g']

            s_one = None
            s_four = None
            for k in mapping.keys():
                for i in inputs:
                    if k not in i:
                        continue
                    plocs = self._possible_locs(len(i))
                    for s in ['a','b','c','d','e','f','g']:
                        if s in mapping[k] and s not in plocs:
                            mapping[k].remove(s)
                if len(mapping[k]) == 2:
                    s_one = mapping[k]
                if len(mapping[k]) == 3:
                    s_four = k

            mapping[s_four].remove(s_one[0])
            mapping[s_four].remove(s_one[1])

            # print(mapping)
                
            segments = {}
            for s in ['a','b','c','d','e','f','g']:
                segments[s] = []
                for k, v in mapping.items():
                    if s in v:
                        segments[s].append(k)
            return segments
