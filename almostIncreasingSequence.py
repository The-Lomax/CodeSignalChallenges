# Given a list of ints, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the list.

# Note: strictly increasing sequence is when each consecutive element is larger than previous one

def solution(sequence):
    if len(sequence) == 1:
        return True
    else:
        removed = 0
        size = len(sequence)
        i = 1
        while i < size:
            if sequence[i] > sequence[i - 1]:
                i += 1
            else:
                if i > 1:
                    if sequence[i] > sequence[i - 2]:
                        sequence.pop(i - 1)
                    else:
                        sequence.pop(i)
                else:
                    sequence.pop(i - 1)
                size = len(sequence)
                removed += 1
                if removed > 1:
                    return False
        return True

data = [10, 1, 2, 3, 4, 5]

if __name__ == "__main__":
    print(solution(data))
