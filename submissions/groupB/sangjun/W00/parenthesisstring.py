import sys
n = int(sys.stdin.readline())
sum =0
for i in range(n):
    string = sys.stdin.readline()
    for k in string:
        if k=='(':
            sum+=1
        elif k == ')':
            sum-=1
            if sum == -1:   
                print('NO')
                break
    if sum ==0:
        print('YES')
    elif sum > 0 :
        print('NO')
    sum = 0

        
        

        



 

    

