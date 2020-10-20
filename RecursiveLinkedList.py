"""
PROJECT 2 - Recursion
"""

from Project2.LinkedNode import LinkedNode


def insert(value, node=None):
    '''Function which initializes a linked list if no node present,
    or inserts a new node into already existing list'''
    new_node = LinkedNode(value, node)
    if node is None:
        return new_node
    elif new_node.value < node.value:
        return new_node
    else:
        node.next_node = insert(value, node.next_node)
        return node

def string(node):
    '''Function which takes in a linked list and returns a string representation of the list ''' 
    if node is None:
        return ""
    elif node.next_node is not None:
        return str(node.value)+ ", " + string(node.next_node)
    else:
        return str(node.value) + string(node.next_node)

def reversed_string(node):
    '''Function that takes in a linked list and returns a reversed string representation'''
    if node is None:
        return ""
    elif node.next_node is not None:
        return reversed_string(node.next_node) + ", " + str(node.value)
    else:
        return reversed_string(node.next_node) + str(node.value)

def remove(value, node):
    ''' Function which takes in a value and linked list,
    then removes the first value found in the list which is equal to the input value'''
    if node is None:
        return node
    elif value == node.value:
        return node.next_node
    else:
        node.next_node = remove(value, node.next_node)
        return node

def remove_all(value, node):
    '''Function that takes in a value and linked list, removes
    every value found in the list, that is equal to the input value '''
    if node is None or value < node.value:
        return node
    elif value == node.value:
        return remove_all(value, node.next_node)
    else:
        node.next_node = remove_all(value, node.next_node)
        return node

def search(value, node):
    """ Looks for value in list starting with head node
Returns True if the value is in the list and False if it is not in the list"""
    if node is None:
        return False`
    elif node.value == value:
        return True
    else:
        return search(value, node.next_node)

def length(node):
    '''Function which takes in a linked list and calculates the length of it'''
    if node is None:
        return 0
    else:
        return 1 + length(node.next_node)

def sum_all(node):
    '''Function which calculates the sum of the values in the list'''
    if node is not None:
        return int(node.value) + sum_all(node.next_node)
    else:
        return 0

def count(value, node):
    '''Function that counts the number of times
an input value appears int he input linkedlist'''
    if node is None:
        return int(0)
    elif node.value == value:
        return int(1) + count(value, node.next_node)
    else:
        return count(value, node.next_node)
    
