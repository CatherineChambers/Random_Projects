from functools import reduce


def add_num(b, c):
    return b + c


a = [1, 2, 3, 10]
print(reduce(add_num, a))


class NumberName:
    def __init__(self, number, name):
        self.name = name
        self.number = number


a = NumberName(5 * 8, "Idowu")
b = getattr(a, 'name')
print(b)