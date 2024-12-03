from aocd import get_data, submit

day = 4
year = 2024
data = get_data(day=day, year=year)

lines = data.split("\n")
answer = None



submit(answer, part="a", day=day, year=year)