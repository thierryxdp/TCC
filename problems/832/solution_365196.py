def eh_quadrada(matriz):
    linhas=len(matriz)
    lista=[]
    for i in range(len(matriz)):
        if linhas!=len(matriz[i]):
            return False
    return True