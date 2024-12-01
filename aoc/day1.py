from itertools import starmap
from aocd import get_data, submit

day = 1
year = 2024
data = get_data(day=day, year=year)

number_pairs = data.split("\n")

def split_pair(pair):
    [a, b] = pair.split("   ")
    return [int(a), int(b)]

def unzip(zipped_list):
    return zip(*zipped_list)

def distance(a, b):
    return abs(a - b)

number_pairs = list(map(split_pair, number_pairs))
left, right = unzip(number_pairs)

left_sorted = sorted(left)
right_sorted = sorted(right)

sorted_zipped = zip(left_sorted, right_sorted)

distances = list(starmap(distance, sorted_zipped))
sum_distances = sum(distances)

submit(sum_distances, part="a", day=day, year=year)

def similarity_right(number):
    count_right = right_sorted.count(number)
    return number * count_right

counted_multiplied = list(map(similarity_right, left_sorted))
counted_sum = sum(counted_multiplied)
submit(counted_sum, part="b", day=day, year=year)