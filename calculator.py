import operator

# ID 84626897
CALCULATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}


class Stack:
    def __init__(self):
        self.__array = []

    def push(self, value):
        self.__array.append(value)

    def pop(self):
        if not self.__array:
            raise IndexError("Empty stack")
        return self.__array.pop()


def polska_calculator(stack, expression, valuetype=int,
                      calculations=CALCULATIONS):
    for value in expression:
        try:
            if calculations.get(value):
                left, right = stack.pop(), stack.pop()
                stack.push(calculations[value](right, left))
            else:
                stack.push(valuetype(value))
        except ValueError:
            raise ValueError(f"value *{value}* is "
                             f"an inappropriate valuetype - "
                             f"*{type(value).__name__}*")
    return stack.pop()


if __name__ == "__main__":
    stack = Stack()
    expression = input().split()
    print(polska_calculator(stack, expression))
