"""
# Project 4
# Name:Sabrina Garcia
# PID:A42006407
"""

class Stack:
    """
    Stack class
    """
    def __init__(self, capacity=2):
        """
        DO NOT MODIFY
        Creates an empty Stack with a fixed capacity
        :param capacity: Initial size of the stack. Default size 2.
        """
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.size = 0

    def __str__(self):
        """
        DO NOT MODIFY
        Prints the values in the stack from bottom to top. Then, prints capacity.
        :return: string
        """
        if self.size == 0:
            return "Empty Stack"

        output = []
        for i in range(self.size):
            output.append(str(self.data[i]))
        return "{} Capacity: {}".format(output, str(self.capacity))

    def __eq__(self, stack2):
        """
        DO NOT MODIFY
        Checks if two stacks are equivalent to each other. Checks equivalency of data and capacity
        :return: True if equal, False if not
        """
        if self.capacity != stack2.capacity:
            return False

        count = 0
        for item in self.data:
            if item != stack2.data[count]:
                return False
            count += 1

        return True

    def stack_size(self):
        '''
        Function that finds the size of a stack
        :return: the size of the stack 
        '''
        return self.size

    def is_empty(self):
        '''
        Function that determines if stack is Empty
        :return: Boolean, True if empty 
        '''
        if self.size == 0:
            return True
        else:
            return False

    def top(self):
        '''
        Function to see top value of stack
        :return: the top value of the stack
        '''
        if not self.is_empty():
            return self.data[self.size-1]
        if self.is_empty():
            return None

    def push(self, val):
        '''
        Function to put new value into stack
        :param val: the value to put in stack 
        :return: nothing
        '''
        if self.capacity == self.size:
            self.grow() #self auto passed in
            self.data[self.size] = val
            self.size += 1
                
            #pushed_val = self.data[-1]

    def pop(self):
        '''
        Function to remove value from the stack
        :param: stack
        :return: the value that was removed
        '''
        if not self.is_empty():
            self.size -= 1
            popped_val = self.data[self.size]
            self.data[self.size] = None
            if self.size <= (self.capacity // 2) and self.capacity != 2:
                self.shrink()
            return popped_val
        else:
            return None
        
            
    def grow(self):
        '''
        Function to grow the capacity 
        :return: nothing
        '''
        if self.size == self.capacity:
            self.capacity = self.capacity * 2 
        new_arry = []
        for i in range (0,self.capacity):
            new_arry.append(None)
        for i in range(0, self.size):
            new_arry[i] = self.data[i]
        self.data = new_arry

    def shrink(self):
    '''
    Function that shrinks the capacity
    :return: nothing
    '''
        self.capacity = self.capacity // 2
        new_arry = []
        for i in range (0,self.size):
            new_arry.append(self.data[i])
        self.data = new_arry
        
def reverse(stack):
    '''
    Function to reverse the Stack
    :return: returns a new stack that is reversed 
    '''
    reversed_stack = Stack() # this creates a new stack class
    my_size = stack.size
    for i in range (0, my_size):
        reversed_stack.push(stack.pop())
    return reversed_stack

def replace(stack, old, new):
    '''
    Function that creates a new stack with replacements
    :param old: the value to change with a new value
    :param new: new value to replace old value
    '''
    replaced_stack = Stack() # create a new stack again
    my_size = stack.size
    for i in range(0, my_size):
        if stack.top() == None
            stack.pop()
        if stack.top() != old:
            replaced_stack.push(stack.pop())
        if stack.top() == old:
            replaced_stack.push(new)
    return reverse(replaced_stack)
