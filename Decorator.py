#!/usr/bin/env python
# coding: utf-8

# In[1]:


YELLOW = '\033[93m'
RED = '\033[91m'
NORMAL = '\033[0m'

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return '{} is {}'.format(self.name, self.age)

class PersonDecorator(Person):

    def __init__(self, person):
        self._person = person

    def __getattr__(self, name):
        return getattr(self._person, name)

    def __str__(self):
        age = self._person.age
        color = NORMAL
        if (age >= 20) and (age <= 30):
            color = YELLOW
        elif age >= 30:
            color = RED
        return '{}{}{}'.format(color, self._person.__str__(), NORMAL)

def main():
    p = []
    
    p.append(Person('Victor', 30))
    p.append(Person('Pablo', 50))
    p.append(Person('Felipe', 55))
    p.append(Person('Amalia', 5))

    for person in p:
        person = PersonDecorator(person)
        print(person)

if __name__ == '__main__':
    main()

