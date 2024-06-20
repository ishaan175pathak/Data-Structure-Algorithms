# Replicating the List class to have an insight of it.

import ctypes

class RecreatingList:
    """ A dynamic array class akin to a simplified Python list.""" 
    def __init__(Ishaan):
        """ 
        Creating an Empty array 
        """
        Ishaan._n = 0                                        # count actual elements
        Ishaan._capacity = 1                                 # default array capacity
        Ishaan._A = Ishaan._make_array(Ishaan._capacity)     # low-level array

    def  __len__(Ishaan):
        """
        Return Number of elements stored in the array
        """
        return Ishaan._n

    def __getitem__(Ishaan,k):
        """
        Return element at index k.
        """
        if not 0 <= k <Ishaan._n:
            raise IndexError('invalid syntax')
        return Ishaan._A[k]                                 # retrieve from array
    
    def append(Ishaan,obj):
        """
        Add object to end of the array 
        """

        if Ishaan._n == Ishaan._capacity:                   # not enough room
            Ishaan._resize(2*Ishaan._capacity)              # double the capacity
        Ishaan._A[Ishaan._n] = obj
        Ishaan._n += 1

    def _resize(Ishaan,c):                                  # nonpublic utility
        """
        Resize internal array to capacity c
        """

        B = Ishaan._make_array(c)                           # new (bigger) array
        for k in range(Ishaan._n):                          # for each existing value
            B[k] = Ishaan._A[k] 
        Ishaan._A = B                                       # use bigger array
        Ishaan._capacity = c

    def _make_array(Ishaan,c):                              # non-public utility
        """
        Return new array with capacity c.
        """
        return (c * ctypes.py_object)()                     # see ctypes documentation

# Almost done.Create a display function to print all the data
