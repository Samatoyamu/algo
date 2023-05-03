from collections import Counter


# ID 83821061
def find_max_points(buttons_pressed, numbers):
    return sum(value <= buttons_pressed for value in Counter(numbers).values())


if __name__ == "__main__":
    buttons_pressed = int(input()) * 2
    numbers = ("".join([input() for value in range(4)])).replace(".", "")
    print(find_max_points(buttons_pressed, numbers))
