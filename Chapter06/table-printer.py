def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        maxLength = 0
        for data in tableData[i]:
            if len(data) > maxLength:
                maxLength = len(data)
        colWidths[i] = maxLength

    for j in range(len(tableData[0])):
        for i in range(len(tableData)):
            print(tableData[i][j].rjust(colWidths[i]), end=' ')
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
