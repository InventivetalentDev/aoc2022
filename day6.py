from util import readInput

inp = readInput('day6')
inp = inp[0]

seen = []
idx = 0
rolling_index = 0
unique = 0
next_is_start = False
for c in inp:

    print("")

    print(c)
    idx += 1
    print("idx", idx)
    print("unique", unique)
    print("seen", seen)

    if c not in seen:
        print("unique")
        seen.append(c)


    else:
        print("not unique")
        seen.append(c)
        # unique-=1

    if len(seen) > 4:
        seen.pop(0)

    unique = set(seen)

    if len(unique) >= 4:
        print("found start!")
        print(seen)
        print(unique)
        print(c)
        print(idx)
        break
