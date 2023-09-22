def melhor_volta(matriz):
    """Pede uma matriz 6x10 representando os tempos
    de 10 voltas de 6 corredores numa pista de kart
    e retorna o melhor corredor com o melhor tempo
    da prova.
    list->tuple"""
    tempos = []
    for i in range(len(matriz)):
        tempos.append(min(matriz[i]))
    melhor_tempo = min(tempos)
    corredor = tempos.index(melhor_tempo) +1
    return (corredor, melhor_tempo)