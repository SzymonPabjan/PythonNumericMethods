# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:07:08 2020

@author: Szymon
"""

import numpy as np
import matplotlib.pyplot as plt

list_matrix = [[6, 5, -5],[2, 6, -2],[2, 5, -1]]
matrix_A = np.array(list_matrix)
st_vect = np.random.randint(-10, 10, 3)

def norma(vect):
    return vect/np.linalg.norm(vect)

new_vect = norma(matrix_A@norma(st_vect))
norm_list = []

for i in range(40):
    new_vect = norma(matrix_A@norma(new_vect))
    norm_list.append(new_vect@matrix_A@new_vect)
 
print("Wektor z własnych obliczen")
#print("")
print(new_vect)
print("")
print("Wartość własna z obliczen")
#print("")
print(new_vect@matrix_A@new_vect)
print("")
print("Wartosci wlasne z funkcji eig()")
print(np.linalg.eig(matrix_A)[0])
print("")
print("Wektory wlasne z funkcji eig()")
print(np.array2string(np.linalg.eig(matrix_A)[1]))
print("")
plt.plot(norm_list)
plt.xlabel("iteracja")
plt.ylabel("wartosc wlasna")