import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return ((3*(x**3))-(4*(x**2))-1)

#def value_check():
#    print("Podaj przedział <a,b>")
#    a=input()
#    b=input()
#    print("Podane przez ciebie wartości to " + a + " i "+b)
#    a_f=float(a)
#    b_f=float(b)
#    if(func(a_f)*func(b_f)<0):
#        print("Podane wartości są poprawne")
#        return True 
#    else:
#        print("Podane wartości są błędne")


def bisection(a,b,epsilon):
    condition = True
    x_0 = a+((b-a)/2)
    
    zero_list = []
    zero_list.append(x_0)
    
    y_zero_list = []
    y_zero_list.append(func(x_0))
    
    return_list = []
    
    while(condition):
        print(x_0)
        condition = True
        zero_list.append(x_0)
        y_zero_list.append(func(x_0))
        if(abs(func(x_0))<epsilon):
            print("Miejsce zerowe to " + str(x_0))
            condition = False
        elif((func(x_0)<0 and func(a)<0) or (func(x_0)>0 and func(a)>0) ):
            a=x_0
            x_0=a+((b-a)/2)
        elif((func(x_0)<0 and func(b)<0) or (func(x_0)>0 and func(b)>0) ):
            b=x_0
            x_0=a+((b-a)/2)
    
    return_list.append(zero_list)
    return_list.append(y_zero_list)
    return return_list

def graph_draw(a,b,list):
    if(a>b):
        main_X = np.arange(b,a, 0.1)
    else:
        main_X = np.arange(a,b, 0.1)
    main_Y = []
    for items in main_X:
        main_Y.append(func(items))
    
    plt.plot(main_X, main_Y)
    plt.plot(list[0],list[1], "o")

def final():
    condition = True
    while(condition):
        print("Podaj przedział <a,b>")
        a=input()
        b=input()
        print("Podane przez ciebie wartości to " + a + " i "+b)
        a_f=float(a)
        b_f=float(b)
        if(func(a_f)*func(b_f)<0):
            print("Podane wartości są poprawne")
            print("Podaj epsilon:")
            epsilon_local = float(input())
            list = bisection(float(a),float(b),epsilon_local)
            graph_draw(float(a),float(b),list)
            condition = False
        else:
            print("Podane wartości są błędne, podaj je jeszcze raz")
            print("")
            condition = True

final()





