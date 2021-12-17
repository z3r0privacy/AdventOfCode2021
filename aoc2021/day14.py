from aoc2021.aocutils import *


class Day14:

    def __init__(self):
        self._day = "14"
        self._isdone = True
        self.lines = read_file_lines(self.Day)

    @property
    def Day(self):
        return self._day

    @property
    def Done(self):
        return self._isdone

    def _prepare(self):
        template = self.lines[0]
        rules = {}
        counts = {}
        for rule in self.lines[2:]:
            a,b = rule.split(" -> ")
            rules[a] = b
            counts[b] = 0
        for c in template:
            counts[c] = 1
        return template, rules, counts

    def _rec_solve(self, pair, rules, remaining):
        if (pair, remaining) in self.cache.keys():
            return self.cache[(pair, remaining)]
        counts = {}
        if remaining == 0:
            return counts
        nc = rules[pair]
        counts[nc] = 1
        c1 = self._rec_solve(pair[0]+nc, rules, remaining-1)
        c2 = self._rec_solve(nc+pair[1], rules, remaining-1)
        for k,v in c1.items():
            if k in counts.keys():
                counts[k] += v
            else:
                counts[k] = v
        for k,v in c2.items():
            if k in counts.keys():
                counts[k] += v
            else:
                counts[k] = v
        self.cache[(pair, remaining)] = counts
        return counts

    def solve_1(self):
        self.cache = {}
        tpl, rules, counts = self._prepare()
        for i in range(len(tpl)-1):
            c1 = self._rec_solve(tpl[i:i+2], rules, 10)
            for k,v in c1.items():
                if k in counts.keys():
                    counts[k] += v
                else:
                    counts[k] = v
        return max(counts.values()) - min(counts.values())
        # first version
        """
        tpl, rules, counts = self._prepare()
        for i in range(10):
            tba = []
            _tpl = "".join(tpl)
            for i in range(len(tpl)-1):
                tba.append(rules[_tpl[i:i+2]])
            idx = 1
            for c in tba:
                tpl.insert(idx, c)
                idx += 2
                counts[c] += 1
        return max(counts.values()) - min(counts.values())
        """
        
    def solve_2(self):
        self.cache = {}
        tpl, rules, counts = self._prepare()
        for i in range(len(tpl)-1):
            c1 = self._rec_solve(tpl[i:i+2], rules, 40)
            for k,v in c1.items():
                if k in counts.keys():
                    counts[k] += v
                else:
                    counts[k] = v
        return max(counts.values()) - min(counts.values())
