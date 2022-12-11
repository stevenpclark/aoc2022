import operator
import numpy as np

from aocd.models import Puzzle

class Monkey:
    def __init__(self, chunk):
        lines = chunk.split('\n')
        for li in lines:
            if 'Starting' in li:
                li = li.split(':')[1]
                self.items = [int(s) for s in li.split(',')]
            elif 'Test' in li:
                self.test_divisor = int(li.split()[-1])
            elif 'true' in li:
                self.true_dest = int(li.split()[-1])
            elif 'false' in li:
                self.false_dest = int(li.split()[-1])
            elif 'Operation' in li:
                parts = li.split()
                if parts[-2] == '+':
                    self.op = operator.add
                else:
                    self.op = operator.mul
                if parts[-1] == 'old':
                    self.operand = None
                else:
                    self.operand = int(parts[-1])

        self.num_inspections = 0


    def inspect(self, reduce_worry):
        worry = self.items.pop(0)
        if self.operand is None:
            worry = self.op(worry, worry)
        else:
            worry = self.op(worry, self.operand)
        if reduce_worry:
            worry = worry // 3
        if worry % self.test_divisor == 0:
            dest = self.true_dest
        else:
            dest = self.false_dest

        self.num_inspections += 1
        return (worry, dest)
        

def run_sim(chunks, num_rounds, reduce_worry):
    monkeys = [Monkey(chunk) for chunk in chunks]
    divisors = [m.test_divisor for m in monkeys]
    shared_divisor = np.product(divisors)

    for _ in range(num_rounds):
        for monkey in monkeys:
            while monkey.items:
                worry, dest = monkey.inspect(reduce_worry)
                if not reduce_worry:
                    worry = worry % shared_divisor
                monkeys[dest].items.append(worry)

        num_inspections = sorted([m.num_inspections for m in monkeys])
        #print(num_inspections)

    num_inspections = sorted([m.num_inspections for m in monkeys])

    return num_inspections[-1]*num_inspections[-2]




def main():
    puzzle = Puzzle(year=2022, day=11)

    chunks = puzzle.input_data.split('\n\n')

    puzzle.answer_a = run_sim(chunks, 20, reduce_worry=True)
    puzzle.answer_b = run_sim(chunks, 10000, reduce_worry=False)

if __name__ == "__main__":
    main()
