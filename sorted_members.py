import sys
import random

def sortedMembers(leghtUsers):
    member1 = random.randint(1, leghtUsers)
    member2= random.randint(1, leghtUsers)
    if member1 == member2: 
        while member1 == member2:
            member2= random.randint(1, leghtUsers)
    
    return [member1, member2]


sys.modules[sortedMembers] = sortedMembers