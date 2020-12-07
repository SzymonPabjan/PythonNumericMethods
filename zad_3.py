import numpy as np
import scipy
import scipy.misc #bez tego importu nie dizała linlang
np.set_printoptions(suppress=True)


first_row = [9, 8, -2, 4, -2]
second_row = [7, -3, -2, 7, 2]
third_row = [2, -2, 2, -7, 6]
fourth_row = [4, 8, -3, 3, -1]
fith_row = [2, 2, -1, 1 ,4]
list_of_lists = [first_row, second_row, third_row, fourth_row, fith_row]


def rozklad(list_of_lists, first_row):
    
    arr = np.array(list_of_lists)
    cols = len(first_row)
    rows = len(list_of_lists)
    if (rows/cols != 1):
        print ("Macierz nie jest kwadratowa")
        
    up_arr = np.empty((rows, cols))
    low_arr = np.eye(rows, cols)
    
    for i in range(cols):
        for j_1 in range(i+1):
            suma_1 = 0
            for k in range(j_1):
                suma_1 += low_arr[j_1][k]*up_arr[k][i]
               
            up_arr[j_1][i] = arr[j_1][i] - suma_1
       
    
        for j_2 in range(i, cols):
            suma_2 = 0
            for k in range(j_2):
                suma_2 += low_arr[j_2][k]*up_arr[k][i]

            low_arr[j_2][i] = (arr[j_2][i] - suma_2)/up_arr[i][i]
        
    print("Macierze obliczone własnym skryptem: ")
    print("macierz wejściowa")
    print(" ")
    print(arr)
    print(" ")
    print("macierz dolna ")
    print(" ")
    print(np.around(low_arr, decimals=2))
    print(" ")
    print("macierz gorna")
    print(" ")
    print(np.around(up_arr, decimals=2))
    print(" ")
    print("Macierze z funkcji scipy.linalg.lu ")
    print(" ")
    print(np.around(scipy.linalg.lu(arr), decimals=2))
    
    up_arr = np.empty((rows, cols)) # te dwie linijki czyszczą macierze, bo się dzieja dziwne rzeczy gdy wywołamy ponownie funkcję
    low_arr = np.eye(rows, cols)    # gdy wywołamy ponownie funkcję bez ich czyszczenia



rozklad(list_of_lists, first_row)






