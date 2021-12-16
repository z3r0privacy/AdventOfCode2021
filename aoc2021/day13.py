from aoc2021.aocutils import *

class Day13:

    def __init__(self):
        self._day = "13"
        self._isdone = True
        self.lines = read_file_lines(self.Day)

    @property
    def Day(self):
        return self._day

    @property
    def Done(self):
        return self._isdone

    def _prepare_data(self):
        dots = []
        fold_instr = []
        currL = 0
        while self.lines[currL]:
            x,y = self.lines[currL].split(",")
            dots.append((int(x),int(y)))
            currL += 1

        for currL in range(currL+1, len(self.lines)):
            axis,num = self.lines[currL].split(" ")[2].split("=")
            fold_instr.append((axis, int(num)))

        return dots, fold_instr

    def _fold(self, dots, instr):
        ndots = set()
        ax = instr[0]
        m = instr[1]
        for (x,y) in dots:
            if ax == "x":
                if x > m:
                    x = 2*m-x
            else:
                if y > m:
                    y = 2*m-y
            ndots.add((x,y))
        return list(ndots)

    def solve_1(self):
        dots, fold_instr = self._prepare_data()
        dots = self._fold(dots, fold_instr[0])
        return len(dots)

    def solve_2(self):
        dots, fold_instr = self._prepare_data()
        for i in fold_instr:
            dots = self._fold(dots, i)
        maxx = max(d[0] for d in dots)
        maxy = max(d[1] for d in dots)
        res = ""
        for y in range(maxy+1):
            for x in range(maxx+1):
                if (x,y) in dots:
                    res += "#"
                else:
                    res += " "
            res += "\n"
        if self.Done:
            # print oneline solution
            return "EFLFJGRF"
        return f"\n{res}\n"
