import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
pi = np.pi

D = 0.1 #współczynnik dyfuzji
L = 1 #długosć
T = 1 #czas schładzania
t_sk = 0 #temp na krańcach
dx = L/30
dt = T/2500
r = D * (dt/(dx**2))

def start_func(x):
    return np.sin(pi*x)

 #przechowuje temp w daneym kroku czasowym
time_u_list = np.zeros([2500,30]) #macierz wszystkich wartosći

for i in range(0,30):
    time_u_list[0,i] = start_func(i*dx)

for t in range(1, 2499):
    for j in range(1, 29):
        time_u_list[t,j] = ((r*time_u_list[t-1,j-1]) + ((1-2*r)*time_u_list[t-1, j]) + (r*time_u_list[t-1,j+1]))
    time_u_list[t+1] = time_u_list[t]

t = np.linspace(0, T, 2500)
x = np.linspace(0, L, 30)
tt, xx = np.meshgrid(x,t)

fig = plt.figure(figsize=(15,7))
ax = fig.add_subplot(1, 2, 1)
ax.pcolormesh(x,t,time_u_list, cmap='coolwarm')
ax.set_xlabel('x')
ax.set_ylabel('t')

ax = fig.add_subplot(122, projection='3d')
ax.plot_surface(tt, xx, time_u_list, cmap='coolwarm')
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('u(x,t)')

plt.show()