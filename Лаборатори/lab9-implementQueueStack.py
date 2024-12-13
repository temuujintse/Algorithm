class MyQueue:

    def __init__(self):
        self.inputstack=[]
        self.outputstack=[]

    def push(self, x: int) -> None:
        self.inputstack.append(x)

    def pop(self) -> int:
        if not self.outputstack:
            while self.inputstack:
                self.outputstack.append(self.inputstack.pop())
        return self.outputstack.pop()

    def peek(self) -> int:
        if not self.outputstack:
            while self.inputstack:
                self.outputstack.append(self.inputstack.pop())
        return self.outputstack[-1]

    def empty(self) -> bool:
        return len(self.outputstack) == 0 and len(self.inputstack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()