my_stack = [] 
print('PUSHING...')
my_stack.append('Task #1')
my_stack.append('Task #2')
my_stack.append('Task #3')

print(f"My STACK after the push:${my_stack}")

my_stack.pop()
print(f"My STACK after the pop:${my_stack}")


print(f"My STACK peeking:${my_stack[-1]}")

class Stack:
    def __init__(self):
        self.values = []
        
    def push(self,value) -> None:
        self.values.append(value)
    def pop(self) ->None:
        if(len(self.values) !=0):
            self.values.pop()   
        else:
            raise IndexError('Pop is not possible in an empty stack') 
        
    def peek(self):
        if(len(self.values))!=0:
            return self.values[-1]
        
s = Stack()

s.push('Software Fundamentals')
s.push('Database')
s.push('Applied algorithm')
print(s)
s.pop()
print(s)

print(s.peek())