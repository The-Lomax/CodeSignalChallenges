# Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

# Given a ticket number n, determine if it's lucky or not.

def solution(n):
    myStr = str(n)
    digits = len(myStr)
    res1 = 0
    res2 = 0
    if digits % 2 == 1:
        return False
    else:
        checks = digits // 2
        for i in range(checks):
            res1 += int(myStr[i])
            res2 += int(myStr[i + checks])
    
    if(res1 == res2):
        return True
    else:
        return False

print(solution(123321))