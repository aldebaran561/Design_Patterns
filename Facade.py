#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class ProductA:
    @staticmethod
    def method():
        return 'Product A'

class ProductB:
    @staticmethod
    def method():
        return 'Product B'

class ProductC:
    @staticmethod
    def method():
        return 'Product C'

class Facade:
    
    def __init__(self):
        self.productA = ProductA()
        self.productB = ProductB()
        self.productC = ProductC()

    def create(self):
        result = self.productA.method()
        result += (' ') + self.productB.method()
        result += (' ') + self.productC.method()
        return result

facade = Facade()
result = facade.create()
print('The result is equal to {}'.format(result))

