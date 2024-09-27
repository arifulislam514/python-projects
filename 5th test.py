"""
# 1
i = 1
while i <= 100:
    print(i)
    i += 1
"""

"""
# 2
j = 100
while j >= 1:
    print(j)
    j -= 1
"""

"""
# 3
n = int(input("Enter a number :"))
i = 1
while i <= 10:
    print(n, "*", i, "=", n*i)
    i += 1
"""

"""
# 4
nums = [1, 4, 9, 16, 25, 30, 37, 40, 49, 50, 60, 74, 79, 84, 87, 100]
ind = 0
while ind < len(nums):
    print(nums[ind])
    ind += 1
"""

"""
# 5
num = (1, 4, 9, 16, 25, 30, 37, 40, 49, 50, 60, 74, 79, 84, 87, 100)
x = 40
k = 0
while k < len(num):
    if num[k] == x:
        print(k)
    k += 1
"""

"""
# 6
num_1 = (1, 4, 9, 16, 25, 30, 37, 40, 49, 50, 60, 74, 79, 84, 87, 100)
for f in num_1:
    print(f)
"""

"""
# 7
num_2 = [1, 3, 5, 6, 4, 7, 12, 34, 43, 23, 56, 46, 76, 12]
x = 12
dex = 0
for v in num_2:
    if v == x:
        print(dex)
    dex += 1
"""

"""
# 8
for i in range(1, 101):
    print(i)
"""

"""
# 9
for i in range(100, 0, -1):
    print(i)
"""

"""
# 10
n = int(input("Enter a number :"))
for i in range(1, 11):
    print(n * i)
"""

"""
# 11
n = 2
sum1 = 0
i = 0
while i <= n:
    sum1 += i
    i += 1
print(sum1)
"""

"""
# 12
n = 1559
fac = 1
for i in range(1, n+1):
    fac *= i
print(fac)
"""

import gmpy2
n = 16000
fac = gmpy2.fac(n)
print(fac)
