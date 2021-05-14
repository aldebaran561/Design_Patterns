#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Strategy
class Fighter:
    def __init__(self, name=None, health=100):
        self.name = name
        self.health = health
        self.fighting_style = Style()

    def attack(self, attacker, defender):
        self.fighting_style.attack(attacker, defender)

    def defend(self, attacker, defender):
        self.fighting_style.defend(attacker, defender)


# Checked
class Capoeira(Fighter):
    def __init__(self, name=None, health=100, fighting_style=None):
        super(Capoeira, self).__init__(name, health)
        self.fighting_style = fighting_style

    def looks(self):
        print('{0.name} has Capoeira style'.format(self))


class Karate(Fighter):
    def __init__(self, name=None, health=100, fighting_style=None):
        super(Karate, self).__init__(name, health)
        self.fighting_style = fighting_style

    def looks(self):
        print('{0.name} has Karate style'.format(self))


class Style:
    def attack(self, opponent):
        pass

    def defend(self, attacker):
        pass


class Angola(Style):
    def __init__(self):
        super(Angola, self).__init__()

    def attack(self, attacker, opponent):
        print('{0.name} attacked to {1.name} in Angola Style'.format(attacker, opponent))

    def defend(self, attacker, opponent):
        print('{0.name} defend from {1.name} in Angola Style'.format(opponent, attacker))


class Regional(Style):
    def __init__(self):
        super(Regional, self).__init__()

    def attack(self, attacker, opponent):
        print('{0.name} attacked to {1.name} in Regional Style'.format(attacker, opponent))

    def defend(self, attacker, opponent):
        print('{0.name} defend from {1.name} in Regional Style'.format(opponent, attacker))


class Shiru(Style):
    def __init__(self):
        super(Shiru, self).__init__()

    def attack(self, attacker, opponent):
        print('{0.name} attacked to {1.name} in Shiru Style'.format(attacker, opponent))

    def defend(self, attacker, opponent):
        print('{0.name} defend from {1.name} in Shiru Style'.format(opponent, attacker))


class Goju(Style):
    def __init__(self):
        super(Goju, self).__init__()

    def attack(self, attacker, opponent):
        print('{0.name} attacked to {1.name} in Goju Style'.format(attacker, opponent))

    def defend(self, attacker, opponent):
        print('{0.name} defend from {1.name} in Goju Style'.format(opponent, attacker))


player1 = Capoeira(name='Felipe', health=100, fighting_style=Regional())
player2 = Karate(name='Pablo', health=100, fighting_style=Goju())


player1.looks()
player2.looks()

player1.attack(player1, player2)
player2.defend(player1, player2)
player2.attack(player2, player1)
player1.defend(player2, player1)

print('{}, which is player 1, changed his style right now'.format(player1.name))
player1.fighting_style = Angola()

player1.attack(player1, player2)

print('{}, which is player 2, changed his style right now'.format(player2.name))

player2.fighting_style = Shiru()
player2.defend(player1, player2)

