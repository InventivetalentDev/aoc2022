from functional import seq

from util import readInput
import pandas as pd

inp = readInput('day5')

starting_layout = []
moves = []

parseMoves = False
for line in inp:
    if line == '':
        parseMoves = True
        continue

    if parseMoves:
        split = line.split(' ')
        moves.append([int(split[1]), int(split[3]), int(split[5])])
    else:
        i = 0
        row = []
        print(line)
        # line = line.replace(' ', '')
        # if not line.startswith('['):
        #     # column numbers
        #     continue
        while i <= len(line):
            row.append(line[i + 1:i + 2])
            i += 4
        starting_layout.append(row)

print(starting_layout)
print("...")
print(moves)
print()

# convert to DataFrame to pivot
starting_layout = pd.DataFrame(starting_layout)
starting_layout = starting_layout.replace(' ', None).replace('', None)  # drop empty cells
print(starting_layout)
print(starting_layout.shape)

# convert back to individual stacks
stacks = []
for i in range(0, starting_layout.shape[1]):
    lst = starting_layout[i].tolist()
    lst.reverse()
    stacks.append(list(filter(lambda x: x is not None and not x.isnumeric(), lst)))
print(stacks)


def print_stacks():
    highest = seq(stacks).map(lambda s: len(s)).max()
    bottom_up = []
    for r in range(0, highest + 1):
        rw = ''
        for c in range(0, len(stacks)):
            try:
                rw += '[' + stacks[c][r] + ']'
            except IndexError:
                rw += '   '
        bottom_up.append(rw)
    for r in range(len(bottom_up), -1, -1):
        try:
            print(bottom_up[r])
        except IndexError:
            pass
    print("==============")


print_stacks()

part2 = True

## Run Moves
print()
print("Moving...")
for mv in moves:
    amount, source, target = mv
    # to 0-index
    source -= 1
    target -= 1

    if part2:
        removed = stacks[source][-amount:]
        del stacks[source][-amount:]
        print(removed)
        stacks[target].extend(removed)
    else:
        for a in range(0, amount):
            removed = stacks[source].pop(len(stacks[source]) - 1)
            stacks[target].append(removed)

    print_stacks()

# Check top crates
msg = ''
for s in range(0, len(stacks)):
    msg += stacks[s][len(stacks[s]) - 1]

print(msg)
