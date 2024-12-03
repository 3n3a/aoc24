from itertools import combinations
from aocd import get_data, submit

day = 2
year = 2024
part = "a"
data = get_data(day=day, year=year)

def to_levels(report_line):
    levels = report_line.split(" ")
    return list(map(int, levels))

reports_lines = data.split("\n")
reports = list(map(to_levels, reports_lines))

inc = [1, 2, 3]
dec = [-1, -2, -3]

def is_safe(levels):
    # no inc / dec
    if levels[0] == levels[1]:
        return False
    
    not_inc = False
    not_dec = False

    for i, level in enumerate(levels[1:]):
        prev = levels[i]
        if prev - level not in inc:
            not_inc = True
        if prev - level not in dec:
            not_dec = True

    if not_inc and not_dec:
        return False
    else:
        return True
    
def calc_safe_count():
    safe_count = 0
    for report in reports:
        if is_safe(report):
            safe_count += 1
        else:
            if not part == "b":
                continue
            # bruteforce
            level_subsets = combinations(report, len(report) - 1)
            found_safe = False
            for sub in level_subsets:
                if is_safe(sub):
                    found_safe = True
            if found_safe:
                safe_count += 1

    return safe_count

submit(calc_safe_count(), part=part, day=day, year=year)

part = "b"
submit(calc_safe_count(), part=part, day=day, year=year)