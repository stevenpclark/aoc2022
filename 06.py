from aocd.models import Puzzle

def get_marker(s, n):
    for i in range(n,len(s)+1):
        if len(set(s[i-n:i])) == n:
            return i

def main():
    puzzle = Puzzle(year=2022, day=6)

    s = puzzle.input_data

    puzzle.answer_a = get_marker(s, 4)
    puzzle.answer_b = get_marker(s, 14)

if __name__ == "__main__":
    main()
