from aocd import get_data, submit
import regex as re

day = 4
year = 2024
data = get_data(day=day, year=year)

def char_split(s):
    return list(s)

def to_str(a):
    return ''.join(a)

lines = data.split("\n")
chars = []
for line in lines:
    chars.append(char_split(line))

answer = None

q = "XMAS"

def transpose(arr):
    return [*zip(*arr)]

def count_overlapping(text, search_for):
    return len(re.findall(search_for, text, overlapped=True))

def get_diagonals(grid, bltr = True):
  dim = len(grid)
  assert dim == len(grid[0])
  return_grid = [[] for total in list(range(2 * len(grid) - 1))]
  for row in list(range(len(grid))):
    for col in list(range(len(grid[row]))):
      if bltr: return_grid[row + col].append(grid[col][row])
      else:    return_grid[col - row + (dim - 1)].append(grid[row][col])
  return return_grid

vertical = transpose(chars)
vertical_s = list(map(to_str, vertical))

diagonal_top_bottom = get_diagonals(chars, bltr=True) # top left, bottom right
diagonal_bottom_top = get_diagonals(chars, bltr=False) # bottom left, top right

diagnoal_top_bottom_s = list(map(to_str, diagonal_top_bottom))
diagonal_bottom_top_s = list(map(to_str, diagonal_bottom_top))

c = 0
s = lines + vertical_s + diagnoal_top_bottom_s + diagonal_bottom_top_s

rev = q[::-1]
print(q, rev)

for line in s:
    # TODO: horizontal, vertical, diagonal, overlapping find
    c += count_overlapping(line, q)
    c += count_overlapping(line, rev)

print(c)
submit(c, part="a", day=day, year=year)