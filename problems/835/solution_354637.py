def melhor_volta(matriz):
    menores_tempos=[]
    for i in range(len(matriz)):
        list.append(menores_tempos,min(matriz[i]))
    quem=list.index(menores_tempos,min(menores_tempos))+1
    menort=min(menores_tempos)
    volta=list.index(quem,menort+1)
    return quem,menort,volta