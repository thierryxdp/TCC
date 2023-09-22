def busca(elemento,matriz):
    result=[]
    for i in range(len(matriz)):
        if elemento in matriz[i]:
            matriz[i]=matriz[i].remove(elemento)
            result+=[matriz[i]]

    
    return result