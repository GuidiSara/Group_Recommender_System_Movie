import sys
import numpy as np
import math 


def standarditation(group):
    
    mapUser = create_map_user(group)
    return mapUser


def create_map_user(group):
    dictionaryUser = insert_key_and_value(group.users)
    group.data.insert(3, "rating_norm", None, True)
    group.data.insert(4, "standard_deviation", None, True)

    for index, row in  group.data.iterrows():
        dictionaryUser = calculate_x_mean_and_insert_ratings_user(row, dictionaryUser)
        
    mean_tot = np.mean(group.data['rating'])
    dictionaryUser = calculate_standard_deviation(dictionaryUser, mean_tot)

    group = calculate_rating_norm(dictionaryUser, group)

    return dictionaryUser


def insert_key_and_value(users):
    dictionaryUser= {}
    for index , row in users.iterrows():
        key = row['user_id']
        dictionaryUser[key] = {
            "ratings_user": [],
            "x_mean": 0,
            "standard_deviation": 0
        }
    return dictionaryUser



def calculate_x_mean_and_insert_ratings_user(element, dictionaryUser):
    dictionaryUser[element.user_id]['ratings_user'].append(element['rating'])
    dictionaryUser[element.user_id]['x_mean'] = np.mean(dictionaryUser[element.user_id]['ratings_user'])

    return dictionaryUser


    

def calculate_standard_deviation(dictionaryUser, mean_tot):
    for key in  dictionaryUser:
        if len(dictionaryUser[key]['ratings_user']) != 0:  
            summation = sum(pow(dictionaryUser[key]['ratings_user'] - mean_tot, 2))
            dictionaryUser[key]['standard_deviation'] = math.sqrt(summation/(len(dictionaryUser[key]['ratings_user'])-1))
        

    return dictionaryUser


def calculate_rating_norm(dictionaryUser, group):

    for index, row in  group.data.iterrows():
        group.data.at[index, 'standard_deviation'] = dictionaryUser[row['user_id']]['standard_deviation']
        group.data.at[index,'rating_norm'] = ((row['rating'] - dictionaryUser[row['user_id']]['x_mean']) / dictionaryUser[row['user_id']]['standard_deviation'])

    
    return group;     

sys.modules[standarditation] = standarditation