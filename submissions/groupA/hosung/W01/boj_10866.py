import sys
from collections import deque

n = int(sys.stdin.readline())
dq = deque()

for _ in range(n):
    input = sys.stdin.readline().split()
    op = input[0]

    if op == "push_front":
        dq.appendleft(input[1])

    elif op == "push_back":
        dq.append(input[1])

    elif op == "pop_front":
        print(dq.popleft() if dq else -1)

    elif op == "pop_back":
        print(dq.pop() if dq else -1)

    elif op == "size":
        print(len(dq))

    elif op == "empty":
        print(0 if dq else 1)

    elif op == "front":
        print(dq[0] if dq else -1)

    elif op == "back":
        print(dq[-1] if dq else -1)
