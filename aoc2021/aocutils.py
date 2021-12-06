import os

def read_file(day):
    path = os.path.join("Inputs", f"{day}.txt")
    with open(path, "r") as f:
        return f.read()

def read_file_lines(day):
    path = os.path.join("Inputs", f"{day}.txt")
    with open(path, "r") as f:
        return [l.strip() for l in f.readlines()]

def read_file_lines_as_num(day):
    return [int(l) for l in read_file_lines(day) if l]

