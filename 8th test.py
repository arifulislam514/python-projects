"""
# 1 my
class Student:
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def average(self):
        sum1 = self.sub1 + self.sub2 + self.sub3
        avg = sum1 / 3
        print(avg)


s1 = Student("Ariful", 95, 97, 98)
print(s1.name, s1.sub1, s1.sub2, s1.sub3)
print(s1.name, "Your average mark is = ", end=" ")
s1.average()
"""

# 2


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum_ = 0
        for val in self.marks:
            sum_ += val
        print(self.name, "your average mark is :", sum_ / 3)


s1 = Student("Ariful", [96, 94, 98])
s1.get_avg()
