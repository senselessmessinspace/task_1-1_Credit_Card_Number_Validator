
from random import randint

def checkLuhn(number):
    print (number)
    sum = 0 
    parity = len(str(number)) % 2 
    for i, digit in enumerate(int(x) for x in str(number)): 
        if i % 2 == parity: 
            digit *= 2 
            if digit > 9: 
                digit -= 9 
        sum += digit
    return (sum % 10 == 0) & (sum != 0)

"""
def checkLuhn(number):
    digits = list(map(int, number))
    return 0 == sum(digits + [ d + (d > 4) for d in digits[-2::-2] ]) % 10
"""

def line(n=16):
    """
    Формирует рандомное (16значное по умолчанию) число в формате строки, верное по алгоритму Луна.
    """
    list = []
    for x in range(n-1):
        list.append(str(randint(0, 9)))
    
    summ = 0
    parity = n % 2 
    for i, digit in enumerate(list): 
        j = int(digit)
        if i % 2 == parity: 
            j *= 2 
            if j > 9: 
                j -= 9
        summ += j

    if summ % 10 != 0:
        list.append(str(10 - (summ % 10)))
    else:
        list.append('0')
    return ''.join(list)


# print (checkLuhn(line()))

for i in [11]:
    print (i, line(i))