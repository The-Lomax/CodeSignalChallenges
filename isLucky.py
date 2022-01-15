# Given a ticket number, determine if the ticket is lucky. Lucky ticket has even number of digits and sums of both half of digits are the same

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