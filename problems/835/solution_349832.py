def melhor_volta(matriz):
    """recebe uma matriz com os tempos em segundos dos corredores em cada volta e 
    retorna uma tupla informando de quem foi a melhor volta da prova,com qual o tempo
    e em que volta.
    list->tuple"""
    min_linha=[]
    for lista in matriz:
        min_linha.append(min(lista))
    min_matriz=min(min_linha)
    corredor=min_linha.index(min_matriz)+1
    volta=matriz[corredor-1].index(min_matriz)+1
    return (corredor,min_matriz,volta)