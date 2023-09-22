def eh_quadrada(matriz):
    linha=[]
    coluna=[]
    i=0
    if i in matriz:
        linha=len(matriz[i])
        i= i+1 
        if linha==coluna:
            return True
        if linha!=coluna:
            return False