from util import readInput
import pandas as pd

inp = readInput('day8')

rows = []
for l in inp:
    rows.append([int(i) for i in l])

dataframe = pd.DataFrame(rows)
print(dataframe)

inner_visible_count = 0
best_score = 0
print(dataframe.shape)
for x in range(1, dataframe.shape[1] - 1):
    for y in range(1, dataframe.shape[0] - 1):
        v = dataframe.at[y, x]
        visible_sides = 4
        score = 1

        print("")
        print("x", x, "y", y, v)

        for x1 in range(x, -1, -1):  # left
            if x1 == x:
                continue
            if dataframe.at[y, x1] >= v:
                visible_sides -= 1
                print("left", abs(x1 - x))
                score *= abs(x1 - x)
                break
        else:
            print("left edge", x)
            score *= abs(x)  # left edge
        for x1 in range(x, dataframe.shape[0]):  # right
            if x1 == x:
                continue
            print(x1, y, dataframe.at[y, x1])
            if dataframe.at[y, x1] >= v:
                visible_sides -= 1
                print("right", abs(x1 - x))
                score *= abs(x1 - x)
                break
        else:
            print("right edge", abs(dataframe.shape[1] - x) - 1)
            score *= abs(dataframe.shape[1] - x) - 1  # right edge
        for y1 in range(y, -1, -1):  # top
            if y1 == y:
                continue
            if dataframe.at[y1, x] >= v:
                visible_sides -= 1
                print("top", abs(y1 - y))
                score *= abs(y1 - y)
                break
        else:
            print("top edge", abs(y))
            score *= abs(y)  # top edge
        for y1 in range(y, dataframe.shape[1]):  # bottom
            if y1 == y:
                continue
            if dataframe.at[y1, x] >= v:
                visible_sides -= 1
                print("bottom", abs(y1 - y))
                score *= abs(y1 - y)
                break
        else:
            print("bottom edge", abs(dataframe.shape[0] - y) - 1)
            score *= abs(dataframe.shape[0] - y) - 1

        # print("sides", visible_sides)
        # print(row_max,col_max)
        visible = visible_sides > 0
        # print(visible)
        print(score)
        if visible:
            inner_visible_count += 1
        if score > best_score:
            best_score = score

outer_visible_count = (dataframe.shape[0] * 2 + dataframe.shape[1] * 2) - 4  # -4 for corners

visible_count = outer_visible_count + inner_visible_count
print("inner", inner_visible_count)
print("outer", outer_visible_count)
print("total", visible_count)

print("best score", best_score)
