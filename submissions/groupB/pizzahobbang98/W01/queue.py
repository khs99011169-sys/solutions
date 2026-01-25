import sys

n= int(input("반복 수행할 정수를 입력하세요: "))

queue=[]

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue.append(command[1])

    elif command[0] == 'pop':
        
        if len(queue) == 0 :
            print(-1)
        else:
            print(queue[0])
            queue.pop(0)
    
    elif command[0] == 'size':
        print(len(queue))

    elif command[0] == 'empty':
        
        if len(queue) == 0:
            print(1)
        else : 
            print(0)
        
    elif command[0] == 'front':
        
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif command[0] == 'back':

        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

