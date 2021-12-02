from aoc2021 import *

def print_day(d):
    print(f"################## Day {d.Day} ##################")
    print(f"# Solution 1: {d.solve_1()}")
    print(f"# Solution 2: {d.solve_2()}")
    print("############################################")
    print()

def main():
    days = [Day01(), Day02()]

    for d in days:
        if d.Done:
            continue
        print_day(d)

    for d in days:
        if not d.Done:
            continue
        print_day(d)

if __name__ == "__main__":
    main()