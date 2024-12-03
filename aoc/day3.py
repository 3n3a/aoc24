from aocd import get_data, submit

day = 3
year = 2024
data = get_data(day=day, year=year)
# coding=utf8
# the above tag defines encoding for this docume

import re

#regex = r"mul\(([0-9]+),([0-9]+)\)"
regex = r"do\(\)|don\'t\(\)|mul\(([0-9]+),([0-9]+)\)"

test_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

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
    #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    #for groupNum in range(0, len(match.groups())):
     #   groupNum = groupNum + 1
      # 
    #    print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.

answer = sum(mult)
print(mult, answer)
submit(answer, part="b", day=day, year=year)


# do\(\)|don\'t\(\)|mul\(([0-9]+),([0-9]+)\)

# each check if is "mul"
# if do => do_multiply = True
# if dont => do_multiply = False

#same loop but with conditional multiply