def melhor_volta(matriz):
    lista1=[]
    lista2=[]
    for c in range(len(matriz)):
        lista1.append(min(matriz[c]))
        for i in range(len(matriz[c])):
            if matriz[c][i]==min(matriz[c]):
                lista2.append(i+1)
    return (lista1.index(min(lista1))+1, min(lista1),lista2[lista1.index(min(lista1))])