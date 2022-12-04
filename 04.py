from aocd.models import Puzzle

def parse_line(line):
    left, right = line.split(',')
    a,b = [int(s) for s in left.split('-')]
    c,d = [int(s) for s in right.split('-')]
    return a,b,c,d
    

def has_a_full_overlap(line):
    a,b,c,d = parse_line(line)
    return (c>=a and d<=b) or (a>=c and b<=d)

def has_any_overlap(line):
    a,b,c,d = parse_line(line)
    return c<=a<=d or c<=b<=d or a<=c<=b or a<=d<=b

def main():
    puzzle = Puzzle(year=2022, day=4)

    lines = puzzle.input_data.split('\n')

    puzzle.answer_a = sum(has_a_full_overlap(li) for li in lines)
    puzzle.answer_b = sum(has_any_overlap(li) for li in lines)


if __name__ == "__main__":
    main()
