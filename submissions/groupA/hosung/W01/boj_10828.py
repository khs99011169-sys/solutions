import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    str = sys.stdin.readline().split()
    input = str[0]

    if input == "push":
        stack.append(str[1])

    elif input == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif input == "size":
        print(len(stack))
    elif input == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif input == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])