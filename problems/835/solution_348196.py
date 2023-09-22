def melhor_volta(matriz):
    lista=[]
    i=0
    resultados=[]
    for n in matriz:
        v=min(n)
        list.append(lista,v)
    tempo=min(lista)
    kart=list.index(lista,tempo)
    volta=matriz[kart]
    menorvolta=list.index(volta,tempo)
    return kart+1,tempo,menorvolta+1