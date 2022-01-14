# Given an array of strings, return another array containing all of its longest strings.

def solution(inputArray):
    res = []
    for el in inputArray:
        if len(res) == 0:
            res.append(el)
        elif len(el) > len(res[0]):
            res = [el]
        elif len(el) == len(res[0]):
            res.append(el)
        else:
            pass
    return res

data = [
    "abc",
    "eeee",
    "abcd",
    "dcd"
]

if __name__ == "__main__":
    print(solution(data))