import numpy as np
import pandas as pd

class Matrix: 
    def __init__(self, group):
        self.matrix =  create_matrix_users_x_items(group)
        self.user_factors = []
        self.item_factors = []


    


def create_matrix_users_x_items(group):
    matrix_usersXitems = np.zeros((len(group.users), len(group.items)))
    
    for index, row in  group.data.iterrows():
        matrix_usersXitems[row['user_id'] - 1, row['movie_id'] - 1] = row['rating']

    #matrix_usersXitems = pd.DataFrame(matrix_usersXitems)
    return matrix_usersXitems




def factoring_matrix_users_items(class_matrix):

    # calcolare la fattorizzazione SVD della matrice
    U, sigma, Vt = np.linalg.svd(class_matrix.matrix, full_matrices=False)

    # creare la matrice diagonale dei valori singolari
    sigma_matrix = np.diag(sigma)

    # calcolare le matrici degli utenti e degli item
    class_matrix.user_factors = np.dot(U, sigma_matrix)
    class_matrix.item_factors = Vt.T

    # stampare le matrici degli utenti e degli item
    print("Matrice degli utenti:")
    print(class_matrix.user_factors)
    print("Matrice degli item:")
    print(class_matrix.item_factors)
    return class_matrix