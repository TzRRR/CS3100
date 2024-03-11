
def max_depth(boxes):
    lists = []
    for b in boxes:
        b = str(b)
        list = b.split(' x ')
        lists.append(list)

    if len(lists) == 1:
        return 0
    else :
        decending_lists = []
        while (len(lists) != 0):
            maxi = []
            max_first_element = -100
            for l in lists:
                if float(l[0]) > max_first_element:
                    max_first_element = float(l[0])
                    maxi = l
            lists.remove(maxi)
            decending_lists.append(maxi)

    matrix = [[0 for _ in  range(len(boxes))] for _ in  range(len(boxes))]
    col_max = [0] * len(boxes)

    for row in range (0, len(boxes)):
        for col in range (0, len(boxes)):
            if float(decending_lists[row][0]) > float(decending_lists[col][0]) and float(decending_lists[row][1]) > float(decending_lists[col][1]) and float(decending_lists[row][2]) > float(decending_lists[col][2]):
                matrix[row][col] = 2
                col_max[col] = 2



    for i in range (len(boxes)):
        for j in range (len(boxes)):
            if matrix[i][j] != 0:
                if (col_max[i] + 1) > matrix[i][j]:
                    matrix[i][j] = col_max[i] + 1
                    if matrix[i][j] > col_max[j]:
                        col_max[j] = matrix[i][j]


    max_layer = 0
    for m in range(len(boxes)):
        for n in range(len(boxes)):
            if matrix[m][n] > max_layer:
                max_layer = matrix[m][n]
    if max_layer == 0:
        max_layer = max_layer + 1
    return max_layer

