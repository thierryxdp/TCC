def eh_quadrada(matriz):
    valores=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            valores= valores+1
    if (valores/len(matriz))== len(matriz):
        return True
    elif len(matriz)==0:
        return True
    else:
        return False