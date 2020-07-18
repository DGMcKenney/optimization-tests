# time_declare_winner.py
# practice using timeit
# to see if i optimisized someone else's solution to a coding problem
# douglas mckenney

"""
PEP 572 mentions that programmers seem to prefer a single line of code
rather than multiple lines, and to avoid unnecessary levels of indentation.

This reminded me of a coding prompt I completed. My solution was quite
inefficient, but one of the other solutions was very streamlined.
This other solution had an assignment containing an 'if' and an 'else',
so I wondered if splitting those out would improve efficiency.
This is my attempt to answer that question.
"""

import timeit

# my original, inefficient solution
solution1 = '''
def declare_winner1(fighter1, fighter2, firstAttacker):
    if firstAttacker == fighter1.name:
        while True:
            fighter2.health -= fighter1.damagePerAttack
            if fighter2.health <= 0:
                return fighter1.name
            fighter1.health -= fighter2.damagePerAttack
            if fighter1.health <= 0:
                return fighter2.name
    if firstAttacker == fighter2.name:
        while True:
            fighter1.health -= fighter2.damagePerAttack
            if fighter1.health <= 0:
                return fighter2.name
            fighter2.health -= fighter1.damagePerAttack
            if fighter2.health <= 0:
                return fighter1.name
'''

# a solution by another solver
solution2= '''
def declare_winner2(fighter1, fighter2, first_attacker):
    cur, opp = (fighter1, fighter2) if first_attacker == fighter1.name else (fighter2, fighter1)
    while cur.health > 0:        
        opp.health -= cur.damage_per_attack
        cur, opp = opp, cur
    return opp.name
'''

# my change to the above solution
solution2b = '''
def declare_winner3(fighter1, fighter2, first_attacker):
    if first_attacker == fighter1:
        cur, opp = fighter1, fighter2
    else:
        cur, opp = fighter2, fighter1
    while cur.health >= 0:
        opp.health -= cur.damagePerAttack
        cur, opp = opp, cur
    return cur.name
'''

setup = 'from two_fighters import Fighter, declare_winner1, \
        declare_winner2, declare_winner3'

code1 = 'declare_winner1(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew")'
code2 = 'declare_winner2(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew")'
code2b = 'declare_winner3(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew")'

result1 = round(timeit.timeit(stmt = code1,
                    setup = setup,
                    number = 500000), 4)
result2 = round(timeit.timeit(stmt = code2,
                    setup = setup,
                    number = 500000), 4)
result2b = round(timeit.timeit(stmt = code2b,
                    setup = setup,
                    number = 500000), 4)

print(f'My original solution took {result1} seconds for 500,000 iterations.')
print(f'Someone else\'s solution took {result2} seconds for 500,000 iterations.')
print(f'My attempted optimization took {result2b} seconds for 500,000 iterations.')

"""
There is some variation- the fastest method was usually solution1, then
solution 2b, and with solution 2 as the slowest.
"""
