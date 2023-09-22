def melhor_volta(matriz):
    lista=[]
    i=0
    for n in matriz:
        v=min(n)
        list.append(lista,v)
    tempo=min(lista)
    kart=list.index(lista,tempo)
    volta=list.index(matriz[kart+1],tempo)
    return volta