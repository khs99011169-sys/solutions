import sys
n = int(sys.stdin.readline())
queue = []
for i in range(n):
    order = sys.stdin.readline().split()
    if order[0] =='push':
        queue.append(int(order[1]))
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order[0] in ['front', 'back','pop']:
        if len(queue) == 0:
            print(-1)
        elif order[0] == 'pop':
            print(queue.pop(0))
        elif order[0] == 'front':
            print(queue[0])
        elif order[0] == 'back':
            print(queue[len(queue)-1])

        