from functools import reduce


class Calculator:
    def __init__(self, *args):
        self.args = args

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda x, y: x * y, args)

    @staticmethod
    def divide(*args):
        return reduce(lambda x, y: x / y, args)
    #   according to the problem description, the 0 case shouldn't be taken into account

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y, args)




