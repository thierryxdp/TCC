def pontos_por_time(x):
    if x[0][2][0]> x[0][2][1] and [1][2][0]= x[1][2][1]:
      	resultado = {x[0][0]:3}
    elif x[0][2][0]< x[0][2][1] and [1][2][0]= x[1][2][1]:
        resultado = {x[0][1]:3}
    elif x[0][2][0]> x[0][2][1] and [1][2][0]>x[1][2][1]:
        resultado = {x[0][0]:6}
    elif x[0][2][0]< x[0][2][1] and [1][2][0]<x[1][2][1]:
        resultado = {x[0][1]:6}