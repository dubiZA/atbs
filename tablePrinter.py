tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(data):
    colWidths = [0] * len(data)

    for i in range(len(colWidths)):
        for j in range(len(data[i])):
            if colWidths[i] < len(data[i][j]):
                colWidths[i] = len(data[i][j])

    for colNum in range(len(data[0])):
        for rowNum in range(len(data)):
            print(data[rowNum][colNum].rjust(colWidths[rowNum]), end=' ')
        print('\n')




printTable(tableData)