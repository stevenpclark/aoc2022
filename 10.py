from aocd.models import Puzzle

def main():
    puzzle = Puzzle(year=2022, day=10)

    cmds = puzzle.input_data.split('\n')
    num_cmds = len(cmds)

    cycle = 1
    x = 1
    i = 0
    next_cycle = 1
    incr = 0
    sig_sum = 0
    buffer = [[' ']*40 for i in range(6)]
    while True:
        r = (cycle-1)//40
        c = (cycle-1)%40
        if next_cycle == cycle:
            x += incr
            if i >= num_cmds:
                break
            args = cmds[i].split()
            if len(args) == 2:
                incr = int(args[1])
                next_cycle += 2
            else:
                incr = 0
                next_cycle += 1

            i += 1
        if abs(x-c) <= 1:
            buffer[r][c] = '#'
        if ((cycle-20)%40) == 0:
            sig_sum += cycle*x
        cycle += 1

    for row in buffer:
        print(''.join(row))

    puzzle.answer_a = sig_sum
    puzzle.answer_b = 'BUCACBUZ'

if __name__ == "__main__":
    main()
