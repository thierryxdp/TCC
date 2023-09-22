def melhor_volta(matriz):
    lista1 = []
    menor=[]
    minimo=0
    c_linha=0
    c_coluna=0
    for lista in matriz:
        lista1 += [min(lista)]
    return min(lista1)

    # list.index(lista1,min(lista1))=de quem foi a melhor volta    # min(lista1)=melhor volta
    #list.index(lista1,min(lista1))
    #min(lista1)=qual tempo

    #list.append(menor,min(matriz[i]))