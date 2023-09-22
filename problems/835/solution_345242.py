def melhor_volta(matriz):
    tempos=[]
    for linha in matriz:
        for aij in linha:
                list.append(tempos,aij)
                tempo_min= min(tempos)
                if tempo_min in linha:
                    volta= list.index(linha,tempo_min)+1
                    corredor= list.index(matriz,linha)+1
    return corredor,tempo_min,volta