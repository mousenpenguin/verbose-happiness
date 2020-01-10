class MinStack:

    def __init__(self):
        self.stack = []                    
        self.minStack = []                    

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minStack) == 0 or x <= self.minStack[-1]:    
            self.minStack.append(x)
        
    def pop(self) -> None:
        top = self.stack[-1]
        self.stack.pop()
        if top == self.minStack[-1]:         
            self.minStack.pop()
        
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]