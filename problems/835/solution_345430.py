def melhor_volta(matriz):
    """Funcao que recebe uma matriz contendo os tempos em segundos de 6 corredores em uma corridad e 10 voltas;list->tuple"""
    melhor1=[]
    for i in range(len(matriz)):
        melhor1=melhor1+[min(matriz[i])]
        corredor=list.index(melhor1,min(melhor1))
        volta=list.index(matriz[corredor],min(matriz[corredor]))
        tempo=matriz[corredor][volta]
        final=(corredor+1, tempo, volta+1)
    return final