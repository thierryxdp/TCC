def eh_quadrada(matriz):
    resultado=''
    for i in range(len(matriz)):
        x=range(len(matriz))
        for j in range(len(matriz[0])):
            y=range(len(matriz[0]))
            if x!=y:
                resultado=False
            if x==y and x==range(0,0):
                resultado=True
    return resultado