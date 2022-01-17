# Given two strings, find the number of common characters between them.

# Example
# For s1 = "aabcc" and s2 = "adcaa", the output should be
# solution(s1, s2) = 3.

def commonCharactersCount(s1, s2):
    res = 0
    for el in s1:
        if el in s2:
            s2 = s2.replace(el, "", 1)
            res += 1
    
    return res


# This function was added to get minimum difference to make words in lists anagrams.
def getMinimumDifference(a, b):
    # Write your code here
    res = []
    if len(a) != len(b):
        return "lists are different size"
    for i in range(0, len(a)):
        if len(a[i]) != len(b[i]):
            res.append(-1)
        else:
            temp = commonCharactersCount(a[i], b[i])
            res.append(len(a[i]) - temp)
    return res


# Test case
a = ['a', 'jk', 'abb', 'mn', 'abc']
b = ['bb', 'kj', 'bbc', 'op', 'def']


if __name__ == "__main__":
    print(getMinimumDifference(a, b))