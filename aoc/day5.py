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

def is_safe(page, return_bad_indexes = False):
    is_safe = []
    bad_indexes = []
    for rule in rules:
        if rule[0] in page and rule[1] in page:
            # check if rule correctly applied
            v0 = page.index(rule[0])
            v1 = page.index(rule[1])

            cur_safe = v0 < v1
            is_safe.append(cur_safe)

            if cur_safe:
                bad_indexes.append(None)
            else:
                bad_indexes.append([v0, v1])
    
    if return_bad_indexes:
        return all(is_safe), bad_indexes

    return all(is_safe)

bad_pages = []

# compare each rule to each page list
# if rule numbers are contained withing target
for page in pages:    
    if is_safe(page):
        middleIndex = math.ceil(len(page) / 2) - 1
        answer += int(page[middleIndex])
    else:
        bad_pages.append(page)

print(answer)
submit(answer, part="a", day=day, year=year)

# part b
answer2 = 0

def find_bad_page_ordering(page, rules):
    for li, ri in rules:
        try:
            lidx, ridx = page.index(li), page.index(ri)
        except ValueError:
            # Atleast one of the values of this rule is not
            # in the update -- this rule is not violated.
            continue
        if lidx > ridx:
            # Update does not follow order -- returning the errant indices.
            return (lidx, ridx)
    # Update follows all ordering rules.
    return None

def find_correct_page_order(page, rules):
    while (result := find_bad_page_ordering(page, rules)) is not None:
        # Swap the bad items and try again.
        lidx, ridx = result
        page[lidx], page[ridx] = page[ridx], page[lidx]
    return page


fixes_pages = (
    find_correct_page_order(u, rules)
    for u in pages
    if find_bad_page_ordering(u, rules) is not None
)
middle_values = (int(u[len(u) // 2]) for u in fixes_pages)
answer2 = sum(middle_values)

print(answer2)
submit(answer2, part="b", day=day, year=year)