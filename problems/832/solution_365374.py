def eh_quadrada(matriz):
    linha=[]
    coluna=[]
    for i in matriz:
        coluna=len(matriz[i])
        if linha==coluna:
            return True
        if linha!=coluna:
            return False