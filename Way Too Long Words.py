n = input()
if type(n) != int:
    if len(n) > 10:
        print(n[0], end="")
        print(len(n) - 2, end="")
        print(n[len(n) - 1])
    elif len(n) < 10:
        print(n)
else:
    pass
