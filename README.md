import re
import random


def show_words():
    words = input("write any words").split(" ")
    resault = []
    for el in words:

        if el not in resault:
            resault.append(el)

    return resault


# print(show_words())

def bajanarar(a: int):
    resault = []
    for i in range(1, int(a / 2) + 1):
        if a % i == 0:
            resault.append(i)
            i += 1
    return resault


# print(bajanarar(50))

def kataryal(num: int):
    sum = 0
    resault = []
    num = int(input("write number"))
    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            resault.append(i)
            sum += i

    if sum == num:
        return True
    else:
        return False


# print(kataryal(28))

def zip(data1, data2):
    resault = []
    if len(data1) != len(data2):
        return False
    for i in range(len(data1)):
        resault.append(data1[i])
        resault.append(data2[i])

    return resault


# print(zip([1, 2, 3, 4, 5], [10, 20, 30, 40, 50]))

def palindrom():
    words = input("Write words")
    str = re.sub('[^A-Za-z0-9]+', ' ', words).lower().split(' ')
    words = str[::-1]

    if words == str:
        return True
    else:
        return False


# print(palindrom())

def middle():
    nums = (input("input list of numbers: ").split(' '))
    nums = list(int(x) for x in nums)
    nums = sorted(nums)
    midlle = sum(nums) / len(nums)
    low = []
    high = []
    for el in nums:
        if el < midlle:
            low.append(el)
    for el in nums:
        if el > midlle:
            high.append(el)
    return midlle, low, high


# print(middle())

def Game():
    res = []
    for i in range(6):
        x = random.randint(1, 49)
        if x not in res:
            res.append(x)
    return sorted(res)


# print(Game())

def is_sorted():
    res = [int(x) for x in input("input nums: ").split()]
    if sorted(res) == res:
        return True
    elif sorted(res)[::-1] == res:
        return True
    else:
        return False


# print(is_sorted())

def is_sublist(larger: list, smaller: list):
    el = True
    for i in range(len(smaller)):
        try:
            x = larger.index(smaller[i])
            if x + 1 != larger.index(smaller[i + 1]):
                el = False
        except:
            pass
    return el


print(is_sublist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 6]))

