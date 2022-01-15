# Given a list of ints, find the pair of adjacent elements that has the largest product and return that product.

def adjacentElementsProduct(inputArray):
    res = inputArray[0] * inputArray[1]
    for i in range(1, len(inputArray) - 1):
        val = inputArray[i] * inputArray[i + 1]
        if val > res:
            res = val
    return res

data = [1, 6, 3, 7, 2, 4, 6]

if __name__ == "__main__":
    print(adjacentElementsProduct(data))