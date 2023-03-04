import sys
import numpy as np

def factoring_matrix_users_items(class_matrix):

    # calcolare la fattorizzazione SVD della matrice
    U, sigma, Vt = np.linalg.svd(class_matrix.matrix, full_matrices=False)

    # creare la matrice diagonale dei valori singolari
    sigma_matrix = np.diag(sigma)

    # calcolare le matrici degli utenti e degli item
    class_matrix.user_factors = np.dot(U, sigma_matrix)
    class_matrix.item_factors = Vt.T

    
    return class_matrix

    

sys.modules[factoring_matrix_users_items] = factoring_matrix_users_items


