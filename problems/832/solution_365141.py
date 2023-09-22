def conta_matriz(matriz):
    nlinhas = 0
    nElementos = 0
    ncolunas = 0
    for i in range(len(Matriz)):
        nlinhas += 1
        for j in range(len(Matriz[0])):
            nElementos += 1
    ncolunas = (nElementos/nlinhas)
def eh_quadrada(matriz):
    if (conta_matriz(matriz)) = 0:
        return True
    elif:
        return False