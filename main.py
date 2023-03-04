from group import Group
from standarditation import * 
# from matrix_users_x_items import *
#from factoring_matrix_users_items import *
from matrix import *

group = Group()
## eliminare le colonne che non ci danno informazione
group.deleteColun()

## bisgona prima di tutto effettuare una normalizzazione sul rating degli utenti.
print("Dataset users: ")
print(group.users)
print("Dataset data: ")
print(group.data)
print("Dataset items: ")
print(group.items)
print("Dataset data_training: ")
print(group.data_training)
print("Dataset data_test: ")
print(group.data_test)


# bsigona standardizzare le votazioni
#Se un valore è esattamente uguale alla media di tutti i valori della caratteristica, sarà normalizzato a 0. 
# Se è al di sotto della media, sarà un numero negativo, e se è al di sopra della media sarà un numero positivo numero. 
# La dimensione di quei numeri negativi e positivi è determinata dalla deviazione standard della caratteristica originale. 
# Se i dati non normalizzati avevano una deviazione standard ampia, i valori normalizzati saranno più vicini a 0.
# group = standarditation(group)


# creazione una matrice users x items
#matrx_userXitem = create_matrix_users_x_items(group)
matrix_user_item = Matrix(group)
matrix_user_item = factoring_matrix_users_items(matrix_user_item)


# stampare le matrici degli utenti e degli item
print("Matrice degli utenti:")
print(matrix_user_item.user_factors)
print("Matrice degli item:")
print(matrix_user_item.item_factors)


