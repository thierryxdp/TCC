def melhor_volta(matriz):
    menores_tempos=[]
    for i in range(len(matriz)):
        list.append(menores_tempos,min(matriz[i]))
    menort=min(menores_tempos)
    quem=list.index(menores_tempos,menort)+1
    volta=list.index(list(matriz[quem]),menort)+1
    return quem,menort,volta