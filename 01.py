import numpy as np

from aocd.models import Puzzle

def main():
    puzzle = Puzzle(year=2022, day=1)

    s = puzzle.input_data
    groups = s.split('\n\n')
    sums = [sum(np.fromstring(g, dtype=int, sep='\n')) for g in groups]

    puzzle.answer_a = max(sums)

    sums.sort()
    puzzle.answer_b = np.sum(sums[-3:])


if __name__ == "__main__":
    main()
