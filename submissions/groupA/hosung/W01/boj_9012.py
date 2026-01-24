import sys

n = int(sys.stdin.readline())

for _ in range(n):
    input = sys.stdin.readline().strip()
    stack = []

    for i in input:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if not stack:
                stack.append(')')
                break
            else:
                stack.pop()
    if len(stack) != 0:
        print('NO')
    else:
        print('YES')
