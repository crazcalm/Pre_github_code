"""
Creating the fibonacci sequence
"""

def fib(number):
    
    number = int(number)
    stack = [0,1]
    
    while max(stack)<number:
        
        fib1 = len(stack) - 1
        fib2 = len(stack) - 2
        
        stack.append(stack[fib1] + stack[fib2])
        
    print stack
    return stack
        


"""
Re-writing the fib function so that it uses less memory.

"""

def fib2(number):
    
    number = int(number)
    stack = [0,1,0]
    
    while max(stack) < number:
        
        fib1 = stack[0]
        fib2 = stack[1]
        fib3 = fib2 + fib1
        
        stack[2] = fib3
        
        stack[0] = stack[1]
        stack[1] = stack[2]
    
    print max(stack)
    return max(stack)

x = raw_input("Give me a natural number: ")

fib(x)
        
