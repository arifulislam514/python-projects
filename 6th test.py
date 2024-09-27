""""
# 1
def avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg
avg(3, 5, 4)
"""

"""
# 2
alist = ["a", "b", "c", "d", "e", "f"]
def len_list(list):
    print(len(list))
    return list

len_list(alist)
"""

"""
# 3
alist = ["a", "b", "c", "d", "e", "f"]
def print_1(list):
    for item in list:
        print(item, end=" ")

print_1(alist)
"""

"""
# 4
n = int(input("Enter a number :"))
def factorial(x):
    fac = 1
    for i in range(1, x + 1):
        fac *= i
    print(fac)
    
factorial(n)
"""

"""
# 5 even or odd
num = int(input("Enter a number :"))
def ev_odd(y):
    if num % 2 == 0:
        print("Even")
    else:
        print("ODD")
ev_odd(num)
"""

"""
# 6 sum of fast n number with recursion
x = int(input("Enter a number :"))
def sum_n(n):
    if n == 0:
        return 0
    return sum_n(n-1) + n
print(sum_n(x))
"""

"""
# 7 print all element in list with recursive function
list_1 = ["a", "b", "c", "d", 1, 2, 3]


def print_list(list1, index=0):
    if index == len(list1):
        return
    print(list1[index])
    print_list(list1, index + 1)


print_list(list_1)
"""