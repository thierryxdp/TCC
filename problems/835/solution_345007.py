def melhor_volta(matriz):
    """Pede uma matriz 6x10 representando os tempos
    de 10 voltas de 6 corredores numa pista de kart
    e retorna o melhor corredor com o menor tempo
    da prova e a volta correspondente ao menor tempo.
    list->tuple"""
    tempos = []
    voltas = []
    for i in range(len(matriz)):
        melhor_tempo = min(matriz[i])
        melhor_volta = matriz[i].index(melhor_tempo)
        tempos.append(melhor_tempo)
        voltas.append(melhor_volta)
    menor_tempo = min(tempos)
    vencedor = tempos.index(min(tempos))
    volta = voltas[vencedor]
    return (vencedor +1,menor_tempo,volta+1)