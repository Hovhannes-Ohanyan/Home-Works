import collections

# 1
# h = open('numbers.txt', 'r')
# numbers = h.readlines()
# a = 0
# for l in numbers:
#     for i in l:
#         if i.isdigit():
#             a += int(i)

# print("The sum is:", a)

# 2

# with open("fileForRead.txt","r") as firstfile,open("fileForWrite.txt","a") as secondfile:
#     for i in firstfile:
#         firstfile=i.title()
#         secondfile.write(firstfile)


# 3
# a=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,1,2,3,5]
# dictionary={"count":0}
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]==a[j]:
#             dictionary["count"] +=1
# print(dictionary)

# 4
# def symbols():
#     count = 0
#     s = open("fileForRead.txt", "r")
#     for i in s:
#         count+=len(i)
#     return count
# print(symbols())

# 5

# str=input("Please write text:")
# l=""
# for i in range(len(str)):
#     if (i+1)%3==0:
#         continue
#     l+=str[i]
# print(l)

# 6
# def count_of_word():
#     file = open('fileForWrite.txt').read().split(' ')
#     result = ''
#     for word in file:
#         if word not in result:
#             result += word + ' = ' + str(file.count(word)) + '\n'
#         else:
#             pass
#
#     return result
#
#
# print(count_of_word())



# 7
# def square(lst:list):
#     res=[]
#     for i in lst:
#         res.append(pow(i,2))
#     return sorted(res)
# print(square([1,2,3,4,5,6,7]))

# 8
# def getSum(n):
#     sum = 0
#     for num in str(n):
#         sum += int(num)
#     return sum
#
#
# n = 12345
# print(getSum(n))

# 9
# def tarberutyun(n):
#     a=1
#     s=0
#     for num in str(n):
#         s+=int(num)
#         a=a*int(num)
#     return a-s
# print(tarberutyun(12345))


# 10
# def odd(start, end):
#     res = []
#     for i in range(start, end + 1):
#         if i % 2 != 0:
#             res.append(i)
#     return res


