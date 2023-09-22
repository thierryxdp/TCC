def busca(elemento,matriz):
    result=[]
    for i in range(len(matriz)):
        if elemento in matriz[i]:
            matriz[i]=list.remove(matriz[i],elemento)
            result+=[matriz[i]]

    
    return result