# two_fighters.py
# determines the winner of a fight
# douglas mckenney
# codwars, Two fighters, one winner, sensei: Scopula

"""
My solution to the following CodeWars prompt:

Create a function that returns the name of the winner
in a fight between two fighters.

Each fighter takes turns attacking the other and
whoever kills the other first is victorious.
Death is defined as having health <= 0.

Each fighter will be a Fighter object/instance.
See the Fighter class below in your chosen language.

Both health and damagePerAttack (damage_per_attack for python)
will be integers larger than 0. You can mutate the Fighter objects.

The Fighter class was provided.
"""

# Fighter class definition
class Fighter(object):
    """This was written by the kata's sensei."""
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)

    __repr__ = __str__

# declare_winner function- my solution
def declare_winner1(fighter1, fighter2, firstAttacker):
    """
    Here's my inefficient solution to find out who the winer will be.
    It is repetative (two identicate but mirrored-image loops)
    but hey, I'm still learning."""
    if firstAttacker == fighter1.name:
        while True:
            fighter2.health -= fighter1.damage_per_attack
            if fighter2.health <= 0:
                return fighter1.name
            fighter1.health -= fighter2.damage_per_attack
            if fighter1.health <= 0:
                return fighter2.name
    if firstAttacker == fighter2.name:
        while True:
            fighter1.health -= fighter2.damage_per_attack
            if fighter1.health <= 0:
                return fighter2.name
            fighter2.health -= fighter1.damage_per_attack
            if fighter2.health <= 0:
                return fighter1.name


# a solution by another solver
def declare_winner2(fighter1, fighter2, first_attacker):
    cur, opp = (fighter1, fighter2) if first_attacker == fighter1.name else (fighter2, fighter1)
    while cur.health > 0:        
        opp.health -= cur.damage_per_attack
        cur, opp = opp, cur
    return opp.name


# my change to the above solution
def declare_winner3(fighter1, fighter2, first_attacker):
    if first_attacker == fighter1:
        cur, opp = fighter1, fighter2
    else:
        cur, opp = fighter2, fighter1
    while cur.health >= 0:
        opp.health -= cur.damage_per_attack
        cur, opp = opp, cur
    return cur.name
