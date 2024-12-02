from aocd import get_data, submit

day = 2
year = 2024
data = get_data(day=day, year=year)

def to_levels(report_line):
    levels = report_line.split(" ")
    return list(map(int, levels))

reports_lines = data.split("\n")
reports = list(map(to_levels, reports_lines))

# 1. all increasing / all decreasing
# 2. 1, 2, 3 -> only acceptable steps

def get_report_direction(report):
    """report direction (increasing, decreasing, unknown)

    Args:
        reports (_type_): array of numbers
    """
    directions = [] # -1 = dec, 0 = none, 1 = inc
    for i, level in enumerate(report):
        if i+1 < len(report):
            next = report[i+1]
        else:
            continue

        # print(i, level, next, next > level)
        if next > level:
            directions.append(1)
        elif next < level:
            directions.append(-1)
        elif next == level:
            directions.append(0)
    allInc = all(x == 1 for x in directions)
    allDec = all(x == -1 for x in directions)
    # print("inc", allInc)
    # print("dec", allDec)
    if allInc:
        return 1
    elif allDec:
        return -1
    else:
        return 0
    
def get_report_steps(report):
    steps = []
    for i, level in enumerate(report):
        if i+1 < len(report):
            next = report[i+1]
        else:
            continue
        
        steps.append(abs(next - level))
    return steps


def is_report_safe(report):
    direction = get_report_direction(report)
    steps = get_report_steps(report)
    steps_within_limits = all(x >= 1 and x <= 3 for x in steps)
    safe_direction = direction != 0
    return safe_direction and steps_within_limits

safe_reports_count = 0
for report in reports:
    if is_report_safe(report):
        safe_reports_count += 1


submit(safe_reports_count, part="a", day=day, year=year)