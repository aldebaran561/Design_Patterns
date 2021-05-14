#!/usr/bin/env python
# coding: utf-8

# In[3]:


class IChair:

    @staticmethod
    def get_dimmensions():
        """Interface of chairs"""

class BigChair(IChair):

    def __init__(self):
        self.height = 80
        self.width = 80
        self.depth = 80

    def get_dimmensions(self):
        return {'height': self.height, 'width': self.width, 'depth': self.depth}

class MediumChair(IChair):

    def __init__(self):
        self.height = 70
        self.width = 70
        self.depth = 70

    def get_dimmensions(self):
        return {'height': self.height, 'width': self.width, 'depth': self.depth}

class ChairFactory:

    @staticmethod
    def get_chair(type_of_chair):
        try:
            if type_of_chair == 'BigChair':
                return BigChair()
            elif type_of_chair == 'MediumChair':
                return MediumChair()
            raise AssertionError('Chair Not Founded')
        except AssertionError as _e:
            print(_e)

if __name__ == '__main__':
    CHAIR = ChairFactory.get_chair('BigChair')
    print('{}:{}'.format(CHAIR.__class__, CHAIR.get_dimmensions()))
    CHAIR = ChairFactory.get_chair('MediumChair')
    print('{}:{}'.format(CHAIR.__class__, CHAIR.get_dimmensions()))
    CHAIR = ChairFactory.get_chair('SmallChair')
    print('{}:{}'.format(CHAIR.__class__, CHAIR.get_dimmensions()))


# In[ ]:




