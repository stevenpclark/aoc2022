from itertools import zip_longest

from aocd.models import Puzzle

def grouper(iterable, n):
    args = [iter(iterable)] * n
    return zip_longest(*args)

def get_shared_char(s):
    n = len(s)
    s1 = s[:n//2]
    s2 = s[n//2:]
    return (set(s1) & (set(s2))).pop()

def get_priority(c):
    if 'a' <= c <= 'z':
        offset = ord('a')-1
    else:
        offset = ord('A')-27
    return ord(c)-offset

def score_bag(s):
    return get_priority(get_shared_char(s))

def get_badge(s1, s2, s3):
    return (set(s1) & set(s2) & set(s3)).pop()

def get_badge_score(group):
    return get_priority(get_badge(*group))

def main():
    puzzle = Puzzle(year=2022, day=3)

    lines = puzzle.input_data.split('\n')

    puzzle.answer_a = sum(score_bag(li) for li in lines)

    groups = grouper(lines, 3)
    puzzle.answer_b = sum(get_badge_score(g) for g in groups)


if __name__ == "__main__":
    main()
