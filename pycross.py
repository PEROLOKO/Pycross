
import random

def generateMap(width,height):
    map = []
    for h in range(height):
        col = []
        for w in range(width):
            col.append(random.randint(0,1))
        map.append(col)
    return map

def getColumn(map,x):
    column = []
    for row in map:
        column.append(row[x])
    return column

def getRowHints(row):
    hint = []
    num = 0
    for i,x in enumerate(row):
        if x == 1:
            num += 1
            if i == len(row)-1:
                hint.append(num)
        else:
            if num != 0:
                hint.append(num)
            num = 0
    return hint

width = 8
height = 5
map = generateMap(width,height)

for i in map:
    print(f'{getRowHints(i)} - {i}')

for i in range(width):
    column = getColumn(map,i)
    print(f'{column} - {getRowHints(column)}')
