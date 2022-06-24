import random


def reverse():
    num = input("Write numbers")
    return num[::-1]


# print(reverse())

def join():
    num = (1, 2, 3, 4)
    res = " "
    for el in num:
        res += str(el)
    return res


# print(join())

def sum_of_min_max(data: list):
    return max(data) + min(data)


# print(sum_of_min_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

def even_index(data: list):
    res = []
    for i in range(len(data)):
        if data[i] % 2 == 0:
            res.append(i)
    return res


# print(even_index([1, 2, 3, 4, 5, 6, 7, 8, 9]))

def reverse_string():
    str = input("Write  word-")
    res = ""
    for i in range(len(str) - 1, -1, -1):
        res += (str[i])
    return res


# print(reverse_string())


def smallest_prime(n):
    while True:
        t = True
        n += 1
        for j in range(2, int(n / 2) + 1):
            if n % j == 0:
                t = False
        if t:
            return n


# print(smallest_prime(100))


def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (s[n // 2 - 1] / 2.0 + s[n // 2] / 2.0, s[n // 2])[n % 2] if n else None


# print(median([1,2,3,4,5,6,7,8,9,10,11]))

def days(month: int, year):
    if month == 2:
        if year % 4 == 0:
            return 29
        return 28
    if month % 2 == 0 and month != 6:
        return 30
    else:
        return 31


# print(days(2,1998))

def random_passwd(n):
    password = ""
    for i in range(n):
        num = random.randint(33, 126)
        password += chr(num)
    return password


# print(random_passwd(30))

def same_parity(n, *args):
    res = []
    for i in args:
        if i % n == 0:
            res.append(i)
    return res


#print(same_parity(3, 1, 2, 3, 4, 5, 6, 7, 8, 9))
