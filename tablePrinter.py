# I struggled with the logic of this one a bit so ended up looking at
# what several others had done. The logic that I battled with was figuring
# out how to access and then print the data from list 0 list 0, list 1
# list 0, list 2 list 0, etc. I think at one point I had it figured out,
# however, it was printing one after the other instead of in a row. It
# was only after looking at another solution that I realized the simple
# solution of using the 'end' parameter and changing it fron a new line
# to a single space. After that it worked like a charm.
#
# I left figuring out the justification logic until after accomplishing
# The correct printing

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(data):
    colWidths = [0] * len(data)

# Some examples I looked at made use of the max() function to achieve
# what I did through the if statement here. Using that function is probably
# more efficient, however, I wanted to use only what I have officially
# learned through Automate the Boring Stuff up to this point. The max()
# Function has not yet (not sure if it will be) been covered.

    for i in range(len(colWidths)):
        for j in range(len(data[i])):
            if colWidths[i] < len(data[i][j]):
                colWidths[i] = len(data[i][j])

    for colNum in range(len(data[0])):
        for rowNum in range(len(data)):
            print(data[rowNum][colNum].rjust(colWidths[rowNum]), end=' ')
        print('\n')




printTable(tableData)