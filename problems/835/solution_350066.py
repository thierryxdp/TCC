def melhor_volta(matriz):
    lista1 = []
    menor=[]
    minimo=0
    c_linha=0
    c_coluna=0
    for lista in matriz:
        lista1 += [min(lista)]
    return list.index(lista1,min(lista1))

    # min(lista1)=melhor volta
    # index(lista1,min(lista1))
    #list.append(menor,min(matriz[i]))