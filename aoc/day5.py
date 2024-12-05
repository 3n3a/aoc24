from aocd import get_data, submit
import math

day = 5
year = 2024
data = get_data(day=day, year=year)

def rule_split(s):
    return s.split("|")

def page_split(s):
    return s.split(",")

sections = data.split("\n\n")
rules = list(map(rule_split, sections[0].split("\n")))
pages = list(map(page_split, sections[1].split("\n")))
answer = 0

# compare each rule to each page list
# if rule numbers are contained withing target
for page in pages:
    is_safe = []
    for rule in rules:
        if rule[0] in page and rule[1] in page:
            # check if rule correctly applied
            v0 = page.index(rule[0])
            v1 = page.index(rule[1])

            is_safe.append(v0 < v1)
    
    if all(is_safe):
        middleIndex = math.ceil(len(page) / 2) - 1
        answer += int(page[middleIndex])

print(answer)
submit(answer, part="a", day=day, year=year)