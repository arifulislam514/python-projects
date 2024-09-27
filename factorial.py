# limit 1558
x = int(input("Enter a number : "))
y = 1
for i in range(1,x+1,1):
    y = y*i
print(x,"! = ",y,sep="")


""""
import gmpy2
n = 16000
fac = gmpy2.fac(n)
print(fac)
"""
