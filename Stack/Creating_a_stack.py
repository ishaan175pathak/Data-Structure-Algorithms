class ArrayStack:
    """
    LIFO Stack implementation using Python list as underlying storage
    """

    def __init__(self):
        """
        Creating an empty list
        """
        self._data = []                         # non public instance
    
    def __len__(self):
        """
        Return the number of elements in the stack
        """

        return len(self._data)
    
    def is_empty(self):
        """
        Return True if the Stack is empty
        """
        return len(self._data) == 0
    
    def push(self, e):
        """
        Add element e to the top of the stack
        """

        self._data.append(e)                    # new item stored at end of list
    
    def top(self):
        """
        Return(But do not remove) the element at the top of the stack

        Raise Empty exception if the stack is empty
        """

        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]                  # the last item in the list
    
    def pop(self):
        """
        Remove and return the element from the top of the stack(i.e. LIFO)

        Raise Empty exception if the stack is empty 
        """

        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._data.pop()                # remove the last item from the list


arr = ArrayStack()
arr.push(5)
arr.push(7)
