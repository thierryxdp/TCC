def busca(elemento,matriz):
    result=[]
    for i in range(len(matriz)):
        if elemento in matriz[i]:
            result+=[matriz[i]]

    
    return result