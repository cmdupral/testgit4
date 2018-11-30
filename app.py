import time


def foo():
    for i in range(101):
        time.sleep(0.3)
        print("\r Loading...{}%".format(i), end="")

foo()