import sys

input = sys.stdin.readline

n = int(input())
q = []

for i in range(n):
    st = input().split()
    if st[0] == 'push': q.append(st[1])
    elif st[0] == 'pop' : print(q.pop(0)) if len(q) != 0 else print(-1)
    elif st[0] == 'size' : print(len(q))
    elif st[0] == 'empty' : print(0) if len(q) != 0 else print(1)
    elif st[0] == 'front' : print(q[0]) if len(q) != 0 else print(-1)
    elif st[0] == 'back' : print(q[-1]) if len(q) != 0 else print(-1)