# Advent of Code 2024

## New Day

* Add in Folder `aoc/day<number>.py`

**Template**:

```python
from aocd import get_data, submit

day = <day>
year = 2024
data = get_data(day=day, year=year)

example_lines = data.split("\n")

submit(answer, part="a", day=day, year=year)
```

## Run Scripts

```bash
poetry run python aoc/day<number>.py
```

# Help

Documentation pages i found helpful.

* [Python Built-in Functions](https://docs.python.org/3/library/functions.html)
* [Python itertools](https://docs.python.org/3/library/itertools.html#itertools.starmap)
* [CyberChef (Selfhosted)](https://cyberchef.enea.tech)