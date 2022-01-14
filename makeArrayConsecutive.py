# Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, 
# each statue having an non-negative integer size. Since he likes to make things perfect, 
# he wants to arrange them from smallest to largest so that each statue will be bigger 
# than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. 
# Help him figure out the minimum number of additional statues needed.

def solution(statues):
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
    print(solution(data))
