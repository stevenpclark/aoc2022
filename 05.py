from copy import deepcopy

from aocd.models import Puzzle

def build_stacks(lines):
    n = (len(lines[0])+1)//4
    stacks = [list() for i in range(n)]
    while lines:
        li = lines.pop()
        for i in range(n):
            c = li[1+i*4]
            if c != ' ':
                stacks[i].append(c)
    return stacks

def main():
    puzzle = Puzzle(year=2022, day=5)

    lines = puzzle.input_data.split('\n')

    stack_input = list()
    stacks = None
    moves = list()
    for li in lines:
        if '[' in li:
            stack_input.append(li)
        elif not stacks:
            stacks = build_stacks(stack_input)
        elif li.startswith('move'):
            n, src, dest = [int(s) for s in li.split()[1::2]]
            src -= 1
            dest -= 1
            moves.append((n, src, dest))

    orig_stacks = deepcopy(stacks)

    for n, src, dest in moves:
        for i in range(n):
            stacks[dest].append(stacks[src].pop())
    puzzle.answer_a = ''.join([st[-1] for st in stacks])

    stacks = orig_stacks
    for n, src, dest in moves:
        chunk = stacks[src][-n:]
        stacks[dest].extend(chunk)
        stacks[src] = stacks[src][:-n]
    puzzle.answer_b = ''.join([st[-1] for st in stacks])


if __name__ == "__main__":
    main()
