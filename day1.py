from functional import seq

from util import readInput

inp = readInput('day1')
print(inp)

sums = []
curr = 0
for line in inp:
    if line == '':
        sums.append(curr)
        curr = 0
        continue

    curr += int(line)

top = seq(sums) \
    .sorted(reverse=True)

print('top', top)

top3 = seq(top) \
    .take(3) \
    .sum()
print('top 3 sum', top3)
