#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from abc import abstractmethod

class Iterator:

    @staticmethod
    @abstractmethod
    def has_next():
        """Returns a bolean whether at end of collection or not"""

    @staticmethod
    @abstractmethod
    def next():
        """Return the object in the collection"""

class Iterable(Iterator):
    
    def __init__(self):
        self.index = 0
        self.max = 4

    def next(self):
        if self.index < self.max:
            x = self.index
            self.index += 1
            return x
        else:
            raise Exception("This is imposible")

    def has_next(self):
        return self.index < self.max

iterable = Iterable()
print(iterable.next())
print(iterable.next())
print(iterable.next())

