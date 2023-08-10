
import random
import math

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

def printMap(map):

    # variaveis
    width = len(map[1])
    maxRowHint = math.ceil(width/2)
    height = len(map)
    columnHints = []
    maxColumnHint = math.ceil(height/2)
    space = "  " * (maxRowHint+1)

    # pegar dicas verticais
    for i in len(map[1]):
        columnHints.append(getRowHints(map))

    # prints horizontal
    for row in map:
        rowHint = getRowHints(row)
        rowHintStr = ""
        rowStr = ""

        # printa as dicas
        for i in range(maxRowHint):
            if i > len(rowHint)-1:
                rowHintStr += "  "
            else:
                rowHintStr += f"{rowHint[i]} "
            
        # printa a linha
        for i in row:
            rowStr += f"[{i}]"
        print(f"{rowHintStr}: {rowStr}")
        

width = 8
height = 5
map = generateMap(width,height)

printMap(map)

#for i in range(width):
#    column = getColumn(map,i)
#    print(f'{column} - {getRowHints(column)}')
