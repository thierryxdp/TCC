def melhor_volta(matriz):
    """A funcao verifica qual kart foi mais rapido, qual foi
    o tempo e em qual volta o atingiu; list-->tuple"""
    lista = []
    i = 0
    for n in matriz:
        v = min(n)
        list.append(lista,v)
    tempo = min(lista)
    kart = list.index(lista,tempo)
    volta = matriz[kart]
    menorvolta = list.index(volta,tempo)
    return kart + 1, tempo, menorvolta+1