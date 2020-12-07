# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 10:19:50 2020

@author: romea
"""
import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [52,5,-5,-40,10]

n = len(x)
m = 3 #stopień wielomianu
x_sum = []
b = []
A = np.empty([m+1,m+1])

for j in range((2*m)+1):
    x_sum.append(sum(np.power(x,j))) # to działa
    
for j in range(m+1):
    for i in range(m+1):
        A[i][j] = x_sum[i+j]
        #print(x_sum[i+j])
    b.append(sum(np.power(x,j)*y))

a = np.linalg.solve(A, np.array(b))
#print(a)
x_numeryczne = np.arange(0, 5, 0.01)
y_numeryczne = []
for x_l in x_numeryczne:
    y_numeryczne.append(np.power(x_l,3)*a[3]+np.power(x_l,2)*a[2]+x_l*a[1]+a[0])
        
plt.plot(x_numeryczne, y_numeryczne)
plt.scatter(x,y, color = 'red')
plt.title("Aproksymacja wielomianu")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


