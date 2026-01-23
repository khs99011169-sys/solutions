class Stack:
    def __init__(self):
        self.items = []

    def push(self, x) :
        self.items.append(x)
    
    def pop(self) : 
        return self.items.pop() if len(self.items) != 0 else -1
        
    
    def size(self) :
        return len(self.items)
    
    def empty(self) :
        return 1 if len(self.items) == 0 else 0
    
    def top(self) :
        return self.items[-1] if len(self.items) != 0 else -1

input_data = int(input())
stack = Stack()

output = []

for _ in range(input_data) :
    input_func = input().split()

    if input_func[0] == "push" :
        stack.push(int(input_func[1]))
    
    elif input_func[0] == "pop" :
        output.append(str(stack.pop()))
    
    elif input_func[0] == "size" :
        output.append(str(stack.size()))

    elif input_func[0] == "empty" :
        output.append(str(stack.empty()))
    
    elif input_func[0] == "top" :
        output.append(str(stack.top()))

    
print('\n'.join(output))