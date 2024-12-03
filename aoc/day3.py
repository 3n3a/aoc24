from aocd import get_data, submit

day = 3
year = 2024
data = get_data(day=day, year=year)

import re


def part_a(data):
    regex = r"mul\(([0-9]+),([0-9]+)\)"

    matches = re.finditer(regex, data, re.MULTILINE)

    mult = []
    for match in matches:
        groups = list(match.groups())
        left = int(groups[0])
        right = int(groups[1])
        mult.append(left * right)

    answer = sum(mult)
    print(mult, answer)
    submit(answer, part="a", day=day, year=year)

def part_b(data):
    regex = r"do\(\)|don\'t\(\)|mul\(([0-9]+),([0-9]+)\)"

    matches = re.finditer(regex, data, re.MULTILINE)

    mult = []
    do_mult = True
    for match in matches:
        # mul(1,2)
        if "mul" in str(match) and do_mult:
            groups = list(match.groups())
            left = int(groups[0])
            right = int(groups[1])
            mult.append(left * right)

        if "don" in str(match):
            do_mult = False

        elif "do" in str(match):
            do_mult = True

    answer = sum(mult)
    print(mult, answer)
    submit(answer, part="b", day=day, year=year)

part_a(data)
part_b(data)