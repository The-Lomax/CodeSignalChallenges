# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

def solution(inputArray):
    res = inputArray[0] * inputArray[1]
    for i in range(1, len(inputArray) - 1):
        val = inputArray[i] * inputArray[i + 1]
        if val > res:
            res = val
    return res

data = [1, 6, 3, 7, 2, 4, 6]

if __name__ == "__main__":
    print(solution(data))