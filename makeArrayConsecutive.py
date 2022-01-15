# Given list of ints, find a minimum number of elements that need adding to the array, 
# so that every consecutive element will be higher than previous one by 1

def makeArrayConsecutive(statues):
    res = 0
    if len(statues) == 1:
        return 0
    else:
        statues.sort()
        for i in range(1, len(statues)):
            res += statues[i] - statues[i - 1]
            res -= 1
    return res

data = [1, 6, 3, 7, 2, 4, 6]

if __name__ == "__main__":
    print(makeArrayConsecutive(data))
