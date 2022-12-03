from util import readInput

inp = readInput('day3')

lowercase_offset = 97
uppercase_offset = 65


def charid(c: str) -> int:
    is_upper = c.isupper()
    cid = ord(c)
    if is_upper:
        return cid - uppercase_offset + 27
    return cid - lowercase_offset + 1


def part1():
    sum = 0
    for rucksack in inp:
        comp1, comp2 = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
        common = 0
        for c1 in comp1:
            for c2 in comp2:
                if c1 == c2:
                    common = charid(c1)
                    break
            else:  # TIL this is a thing https://stackoverflow.com/a/654002/6257838
                continue  # only executed if the inner loop did NOT break
            break  # only executed if the inner loop DID break
        print(common)
        sum += common

    print(sum)


def part2():
    sum = 0
    for i in range(0, len(inp), 3):
        a = set(inp[i])
        b = set(inp[i + 1])
        c = set(inp[i + 2])
        x = a & b & c  # this is very neat.
        print(x)
        sum += charid(x.pop())
    print(sum)


part2()
