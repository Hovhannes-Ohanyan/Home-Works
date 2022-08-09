#1
# def encypt_func(txt, s):
#     result = ""
#
#     for i in range(len(txt)):
#         char = txt[i]
#
#         if (char.isupper()):
#             result += chr((ord(char) + s - 64) % 26 + 65)
#
#         else:
#             result += chr((ord(char) + s - 96) % 26 + 97)
#     return result
#
#
# txt = "hello"
# s = 5
#
# print("Plain txt : " + txt)
# print("Shift pattern : " + str(s))
# print("Cipher: " + encypt_func(txt, s))

#2
# n=0
# for i in range(1,1001):
#     if i%3==0 or i%5==0:
#         n+=i
# print(n)


# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1 or n==2:
#         return 1
#     elif n>2:
#         return (fibonacci(n-1)+fibonacci(n-2))
#
#
# fib_list=[fibonacci(n) for n in range (1, 33) if fibonacci(n)%2==0]
# fib_even=sum(fib_list)
# print(fib_even)