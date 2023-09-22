def melhor_volta(matriz):
    lista1=[]
    lista2=[]
    b=0
    for c in range(len(matriz)):
        for i in range(len(matriz[c])):
            lista2.append(c)
            lista1.append(min(matriz[c]))
    return (min(lista1),lista2)