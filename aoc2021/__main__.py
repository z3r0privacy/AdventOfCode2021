from aoc2021 import *

def print_day(d):
    print(f"################## Day {d.Day} ##################")
    print(f"# Solution 1: {d.solve_1()}")
    print(f"# Solution 2: {d.solve_2()}")
    print("############################################")
    print()

def main():
    days = []
    module = __import__("aoc2021")
    for i in range(1,26):
        name = f"Day{i:02d}"
        try:
            cl = getattr(module, name)
            days.append(cl())
        except AttributeError:
            """Day not (yet) implemented"""

    for d in days:
        if d.Done:
            continue
        print_day(d)

    if any(not d.Done for d in days):
        exit()

    for d in days:
        if not d.Done:
            continue
        print_day(d)

if __name__ == "__main__":
    main()