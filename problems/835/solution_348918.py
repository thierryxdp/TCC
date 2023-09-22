def melhor_volta(matriz):
    """Recebe uma matriz 6x10 e retorna uma tupla com os dados/list->tuple"""
    lista=list()
    for i in range(len(matriz)):
        x=min(matriz[i])
        y=matriz[i].index(x)
        lista.append([x,y])
        lista1=list()
        lista2=list()
    for i in range(len(lista)):
        lista1.append(lista[i][0])
        lista2.append(lista[i][1])
        z=min(lista1)
        w=lista1.index(z)
        v=lista2[w]
        tupla=(w+1,z,v+1)
    return tupla