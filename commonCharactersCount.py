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

if __name__ == "__main__":
    print(commonCharactersCount("aabcc", "adcaa"))