from aocd import get_data, submit

day = 3
year = 2024
data = get_data(day=day, year=year)

import re


def part_a(data):

    regex = r"mul\(([0-9]+),([0-9]+)\)"

    # example data
    # test_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    matches = re.finditer(regex, data, re.MULTILINE)

    mult = []
    do_mult = True
    for matchNum, match in enumerate(matches, start=1):
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
    for matchNum, match in enumerate(matches, start=1):
        
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