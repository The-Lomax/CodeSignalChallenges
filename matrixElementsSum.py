# Given a matrix of ints, where each value represents the cost 
# of the room, return the total cost of all rooms. 

# Add up all the values that don't appear below a 0).

def matrixElementSum(matrix):
    rowsToCheck = set(range(len(matrix[0])))
    rowsToIgnore = set()
    res = 0
    for i in range(len(matrix)):
        for j in rowsToCheck:
            if matrix[i][j] > 0:
                res += matrix[i][j]
            else:
                rowsToIgnore.add(j)
        rowsToCheck = rowsToCheck - rowsToIgnore
        rowsToIgnore = set()
    return res

data = [
    [0, 1, 1, 2], 
    [0, 5, 0, 0], 
    [2, 0, 3, 3]
]

if __name__ == "__main__":
    print(matrixElementSum(data))