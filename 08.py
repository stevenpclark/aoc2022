import numpy as np

from aocd.models import Puzzle

dirs = ((-1, 0), (0, -1), (1, 0), (0, 1))

def main():
    puzzle = Puzzle(year=2022, day=8)

    lines = puzzle.input_data.split()
    g = np.array([[int(c) for c in s] for s in lines], dtype=np.uint8)
    nr, nc = g.shape
    assert nr == nc

    vis = np.zeros((nr, nc), dtype=bool)

    for _ in range(4):
        for r in range(nr):
            prev_max = -1
            for c in range(nc):
                if g[r,c] > prev_max:
                    prev_max = g[r,c]
                    vis[r,c] = True
                    if prev_max >= 9:
                        break
        g = np.rot90(g)
        vis = np.rot90(vis)

    puzzle.answer_a = np.sum(vis)

    max_scenic = 0
    for r in range(1, nr-1):
        for c in range(1, nc-1):
            h = g[r,c]
            scenic_score = 1
            for dr, dc in dirs:
                r2, c2 = r+dr, c+dc
                d = 1
                while (1<=r2<nr-1) and (1<=c2<nc-1) and g[r2,c2] < h:
                    r2 += dr
                    c2 += dc
                    d += 1
                scenic_score *= d
            if scenic_score > max_scenic:
                max_scenic = scenic_score

    puzzle.answer_b = max_scenic

if __name__ == "__main__":
    main()
