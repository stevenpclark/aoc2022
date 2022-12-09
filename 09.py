import numpy as np

from aocd.models import Puzzle

dir_map = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}

def get_tail_visit_count(cmds, num_knots):
    sz = 1000
    v = np.zeros((sz,sz), dtype=bool)
    pos = np.ones((num_knots, 2), dtype=int)*(sz//2)

    v[sz//2, sz//2] = True
    for cmd in cmds:
        d, n = cmd.split()
        dr, dc = dir_map[d]
        n = int(n)
        for _ in range(n):
            pos[0,:] += (dr, dc)
            for ik in range(1,num_knots):
                dist = pos[ik-1,:] - pos[ik,:]
                r_dist, c_dist = dist
                if abs(r_dist) > 1 or abs(c_dist) > 1:
                    pos[ik,:] += [np.sign(r_dist), np.sign(c_dist)]
            tr, tc = pos[-1,:]
            v[tr, tc] = True

    return np.sum(v)

def main():
    puzzle = Puzzle(year=2022, day=9)

    cmds = puzzle.input_data.split('\n')

    puzzle.answer_a = get_tail_visit_count(cmds, 2)
    puzzle.answer_b = get_tail_visit_count(cmds, 10)

if __name__ == "__main__":
    main()
