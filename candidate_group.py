import random
import sys
import numpy as np

def candidate_group_person(ratings):
    people = []
    found = True

    while found:
        person_one = random.randint(1, 943)
        person_two = random.randint(1, 943)
        if(person_one != person_two):
            found = False
            people.append(person_one)
            people.append(person_two)

    return people
        






sys.modules[candidate_group_person] = candidate_group_person