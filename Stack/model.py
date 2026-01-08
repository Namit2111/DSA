class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self,number):
        self.items.append(number)

    def pop(self):
        if self.is_empty():
            print("Nothing in stack")
            return None
        self.items.pop()
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.items[-1]

    def peek_n(self,i):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.items[i]

    def get(self):
        return self.items

if __name__ == "__main__":

    s = Stack()
    s.push(2)
    s.push(3)
    print(s.get())