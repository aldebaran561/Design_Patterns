#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Susbscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print('Hey {}, you got a new message: {}'.format(self.name, message))

class Publisher:
    def __init__(self):
        self.subscribers = set()

    def register(self, name):
        self.subscribers.add(name)

    def unregister(self, name):
        self.subscribers.discard(name)

    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)

pub = Publisher()

#One subscriber
Victor = Susbscriber('Victor')
Juan = Susbscriber('Juan')
Felipe = Susbscriber('Felipe')

pub.register(Victor)
pub.register(Juan)
pub.register(Felipe)

pub.dispatch('This is a salute')

pub.unregister(Juan)

pub.dispatch('This is a discount')

