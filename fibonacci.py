""""
x,y,a,=0,1,1
b = 7
while a<=b:
    total = x+y
    x,y=y,total
    print(total)
    a+=1
"""

"""
a = 5
b = 1
a = b - a
b = b - a
a = a + b
print("a = ",a)
print("b = ",b)


a = 487611
c = 0
find = 1
while a>0:
    b = a % 10
    if b == find:
        c += 1
    a = a // 10
print(c)
"""


a = 98798
b = 0
c = 10
while c >= 10:
    while a > 0:
        b += a % 10
        a = a // 10
    a = b
    c = b
    print(b)
    # print("c",c)
    # print("a",a)
    b = 0
