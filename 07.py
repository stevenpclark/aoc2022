from aocd.models import Puzzle

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children_map = dict()
        self.total_size = None

    def get_size(self):
        if self.total_size is None:
            self.total_size = sum(c.get_size() for c in self.children_map.values())
        return self.total_size

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size


def main():
    puzzle = Puzzle(year=2022, day=7)

    #skip '$ cd /' line
    groups = puzzle.input_data.split('$ ls\n')[1:]

    #each dir will be a dict that maps fn to either int or dict
    #when we ls a dir, need to know if this is new information, or old

    root = Dir('/', None)
    curr_dir = root
    all_dirs = [root]

    for g in groups:
        lines = g.strip().split('\n')
        for li in lines:
            if li.startswith('$'):
                #this is a cd command
                fn = li.split()[2]
                if fn == '..':
                    curr_dir = curr_dir.parent
                    continue
                curr_dir = curr_dir.children_map[fn]
            else:
                #this is one line of ls output
                a, fn = li.split()
                if fn not in curr_dir.children_map:
                    #this is the first time we have ls-ed this dir
                    if a == 'dir':
                        new_dir = Dir(fn, curr_dir)
                        all_dirs.append(new_dir)
                        curr_dir.children_map[fn] = new_dir
                    else:
                        curr_dir.children_map[fn] = File(fn, int(a))

    all_sizes = [d.get_size() for d in all_dirs]
    total_used = sum(all_sizes)

    puzzle.answer_a = sum(sz for sz in all_sizes if sz <= 100000)

    total_disk = 70000000
    min_free = 30000000
    total_used = root.get_size()
    total_free = total_disk - total_used
    need_to_free = min_free - total_free
    puzzle.answer_b = min(sz for sz in all_sizes if sz >= need_to_free)

if __name__ == "__main__":
    main()
