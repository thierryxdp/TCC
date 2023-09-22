def melhor_volta(matriz):
    """recebe uma matriz com os tempos em segundos dos corredores em cada volta e 
    retorna uma tupla informando de quem foi a melhor volta da prova,com qual o tempo
    e em que volta.
    list->tuple"""
    max_linha=[]
    for lista in matriz:
        max_linha.append(max(lista))
    max_matriz=max(max_linha)
    corredor=matriz.index(max_matriz)
    volta=matriz[corredor].index(max_matriz)
    return (correedor,max_matriz,volta)