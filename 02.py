import numpy as np

from aocd.models import Puzzle

THEM_START = ord('A')
US_START = ord('X')

def get_round_score(line, infer_mode=False):
    left, right = line.split()
    them = ord(left) - THEM_START
    us = ord(right) - US_START

    if infer_mode:
        outcome = us
        us = ((them+(outcome-1))%3)
    else:
        outcome = (1+us-them)%3

    shape_score = us+1
    outcome_score = outcome*3

    return shape_score + outcome_score

def main():
    puzzle = Puzzle(year=2022, day=2)

    lines = puzzle.input_data.split('\n')

    puzzle.answer_a = sum(get_round_score(li) for li in lines)
    puzzle.answer_b = sum(get_round_score(li, infer_mode=True) for li in lines)

if __name__ == "__main__":
    main()
