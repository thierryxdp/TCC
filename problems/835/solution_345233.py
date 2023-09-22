def melhor_volta(matriz):
    ''' Função que retorna uma tupla informando qual dos 6 corredores teve a melhor volta da prova, o tempo de prova e em qual volta; list(list)->tuple'''
    for linha in matriz:
        corredor= list.index(matriz,linha)+1
        tempo_min= min(linha)
        volta=list.index(linha,tempo_min)+1
    return corredor,tempo_min,volta