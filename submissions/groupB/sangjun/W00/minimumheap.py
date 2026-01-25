import sys
n = int(sys.stdin.readline())
heap =[]
# x가 자연수이면 배열에 x를 추가 x가 0이면 배열에서 가장 작은값 출력 후 배열에서 제거
#만약 배열이 비어있는 경우에 가장 작은 값을 출력하라는 경우 0을 출력한다.
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap)==0:
            print(0)
        else:
            print(heap.pop(0))
    else:
        heap.append(x)
        heap.sort()



