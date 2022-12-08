from util import readInput
import pandas as pd

inp = readInput('day8')

rows = []
for l in inp:
    rows.append([int(i) for i in l])

dataframe = pd.DataFrame(rows)
print(dataframe)

inner_visible_count = 0
print(dataframe.shape)
for x in range(1, dataframe.shape[0] - 1):
    for y in range(1, dataframe.shape[1] - 1):
        v = dataframe.at[x, y]
        visible_sides = 4
        for x1 in range(0, x):
            if x1 == x:
                continue
            if dataframe.at[x1, y] >= v:
                visible_sides -= 1
                break
        for x1 in range(x, dataframe.shape[0]):
            if x1 == x:
                continue
            if dataframe.at[x1, y] >= v:
                visible_sides -= 1
                break
        for y1 in range(0, y):
            if y1 == y:
                continue
            if dataframe.at[x, y1] >= v:
                visible_sides -= 1
                break
        for y1 in range(y, dataframe.shape[1]):
            if y1 == y:
                continue
            if dataframe.at[x, y1] >= v:
                visible_sides -= 1
                break
        # print(x, y, v)
        # print("sides", visible_sides)
        # print(row_max,col_max)
        visible = visible_sides > 0
        # print(visible)
        if visible:
            inner_visible_count += 1

outer_visible_count = (dataframe.shape[0] * 2 + dataframe.shape[1] * 2) - 4  # -4 for corners

visible_count = outer_visible_count + inner_visible_count
print("inner", inner_visible_count)
print("outer", outer_visible_count)
print("total", visible_count)
