################################
#          프로그램 소개         #
#                              #
# 특정 수 이하의 소수를 전부  출력함#
################################


#Prime number check
#Prime number => return 1
#Not Prime number => return 0 
def checkPrimeNumber(target):
    if target < 2:
        return 0
    elif target == 2 or target == 3:
        return 1
    elif target % 2 == 0:
        return 0
    elif target % 3 == 0:
        return 0
    else:
        i = 5
        while i < target:
            if target % i == 0:
                return 0
            i += 2
        return 1

#input value to checkPrimeNumber()
def inputValue(value):
    result = []
    for i in range(2, value + 1):
        if checkPrimeNumber(i) == 1:
            result.append(i)
    return result

def topPrimeNumber(value):
    i = value
    while i > 0:
        if checkPrimeNumber(i) == 1:
            return i
        i -= 1
    return top

#print(inputValue(1000000))
print(topPrimeNumber(10000000))