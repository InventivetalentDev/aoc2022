from util import readInput

inp = readInput('day4')

subsets = 0
overlap = 0
for pair in inp:
    p1, p2 = pair.split(',')

    p1start, p1end = p1.split('-')
    p2start, p2end = p2.split('-')

    set1 = set(range(int(p1start), int(p1end) + 1))
    set2 = set(range(int(p2start), int(p2end) + 1))

    if set1 | set2 == set1 or set1 | set2 == set2:
        subsets += 1
    if set1 & set2 != set():
        overlap += 1

print(subsets)
print(overlap)

