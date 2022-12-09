import numpy as np

from aocd.models import Puzzle

dir_map = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}

def main():
    puzzle = Puzzle(year=2022, day=9)

    lines = puzzle.input_data.split('\n')
    sz = 1000
    v = np.zeros((sz,sz), dtype=bool)

    num_knots = 2
    pos = np.ones(num_knots, 2)*(sz//2)

    v[pos[-1,:]] = True
    for li in lines:
        d, n = li.split()
        dr, dc = dir_map[d]
        n = int(n)
        for _ in range(n):
            hr += dr
            hc += dc
            r_dist = hr-tr
            c_dist = hc-tc
            if abs(r_dist) > 1 or abs(c_dist) > 1:
                tr += np.sign(r_dist)
                tc += np.sign(c_dist)
            v[pos[-1,:]] = True

    print(np.sum(v))
    #print(v*1)
    #puzzle.answer_a = np.sum(v)
    #puzzle.answer_b = max_scenic

if __name__ == "__main__":
    main()
