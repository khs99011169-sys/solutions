####################################################################################

# 덱
# https://www.acmicpc.net/problem/10866

# 문제
# 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 명령은 총 여덟 가지이다.
# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

####################################################################################

import sys
from collections import deque

dq = deque() # 정수 저장 덱

input = sys.stdin.readline 
n = int(input()) # 입력 수 저장

for i in range(n):
    text = input()
    text = text.split() # 공백으로 명령어와 X 값 나누기
    
    deque_len = len(dq) # deque 의 크기
    
    command = text[0]
    if command == 'push_front' or command == 'push_back': # 명령어가 push_front 이거나 push_back 일 때 뒤에 오는 정수를 변수에 저장
        num = text[1]
        
    if command == "push_front": # 명령어 push_front
        dq.appendleft(num)
    elif command == "push_back": # 명령어 push_back
        dq.append(num)
    elif command == "pop_front": # 명령어 pop_front
        if deque_len == 0:
            print(-1)
        else:
            pop_num = dq[0]
            dq.popleft()
            print(pop_num)
    elif command == "pop_back": # 명령어 pop_back
        if deque_len == 0:
            print(-1)
        else:
            print(dq.pop())      
    elif command == "size": # 명령어 size
        print(deque_len)
    elif command == "empty": # 명령어 empty
        if deque_len == 0:
            print(1)
        else:
            print(0)
    elif command == "front": # 명령어 front
        if deque_len == 0:
            print(-1)
        else:
            print(dq[0])
    elif command == "back": # 명령어 back
        if deque_len == 0:
            print(-1)
        else:
            print(dq[deque_len-1])
    