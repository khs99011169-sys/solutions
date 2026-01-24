import sys

n = int(sys.stdin.readline())
queue = []

for _ in range(n):
    str = sys.stdin.readline().split()
    input = str[0]

    if input == "push":
        queue.append(str[1])

    elif input == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif input == "size":
        print(len(queue))
    elif input == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif input == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif input == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])