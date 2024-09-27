"""
# 1
with open("practice.txt", "w+")as f:
    f.write("Hi everyone \nWe are learning File I/O \nUsing Java. \nI like programing in Java")
"""

"""
# 2
with open("practice.txt", "r") as f:
    data = f.read()
    new_data = data.replace("Java", "Python")
    print(new_data)
"""

"""
# 3
with open("practice.txt", "r") as f:
    word = "learning"
    data = f.read()
    if data.find(word) != -1:
        print("Found")
    else:
        print("Not Found")
"""

"""
# 4
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(line_no)
                return
            line_no += 1

    return -1


print(check_for_line())
"""


# 5 method 1
count = 0
with open("number.txt", "r") as f:
    data = f.read()
    # print(data)
    num = ""
    for i in range(len(data)):
        if data[i] == ",":
            if int(num) % 2 == 0:
                count += 1
            # print(int(num))
            num = ""
        else:
            num += data[i]
print(count)


"""
# 5 method 2
count = 0
with open("number.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    # print(nums)
    for i in nums:
        if int(i) % 2 == 0:
            count += 1
print(count)
"""