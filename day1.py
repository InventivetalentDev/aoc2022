from functional import seq

from util import readInput

inp = readInput('day1')
print(inp)

def asInt(n):
    return int(n)

def sum(n):
    return n+n

sums = []
curr = 0
for line in inp:
    if line=='':
        sums.append(curr)
        curr = 0
        continue

    curr += int(line)

print(seq(sums)\
    .max())