# ID 84578058
class Deque:
    def __init__(self, value):
        self.__queue = [None] * value
        self.__max_size = value
        self.__head = 0
        self.__tail = -1
        self.__size = 0

    def push_front(self, value):
        if self.__size == self.__max_size:
            raise IndexError("Stack is full")
        self.__head = (self.__head - 1) % self.__max_size
        self.__queue[self.__head] = value
        self.__size += 1

    def push_back(self, value):
        if self.__size == self.__max_size:
            raise IndexError("Stack is full")
        self.__tail = (self.__tail + 1) % self.__max_size
        self.__queue[self.__tail] = value
        self.__size += 1

    def pop_front(self):
        if self.__size == 0:
            raise IndexError("Stack is empty")
        value = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_size
        self.__size -= 1
        return value

    def pop_back(self):
        if self.__size == 0:
            raise IndexError("Stack is empty")
        value = self.__queue[self.__tail]
        self.__queue[self.__tail] = None
        self.__tail = (self.__tail - 1) % self.__max_size
        self.__size -= 1
        return value


def commands(cmdnumber, deque):
    for _ in range(cmdnumber):
        cmd, *cmdvalue = input().split()
        try:
            value = getattr(deque, cmd)
            if cmdvalue:
                value(*cmdvalue)
            else:
                print(value())
        except IndexError:
            print("error")
        except AttributeError:
            print("Command not found")


if __name__ == "__main__":
    cmdnumber = int(input())
    max_size = Deque(int(input()))
    commands(cmdnumber, max_size)
