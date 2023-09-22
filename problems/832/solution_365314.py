def eh_quadrada:
    a = 0
    for i in range(len(matriz)):
        if len(matriz) == len(matriz[i-1]):
            a = a+1
        else:
            a = a+0
    if a == len(matriz):
        return True
    else:
        return False