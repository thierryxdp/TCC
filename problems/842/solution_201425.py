def pontos_por_time (L1):
    """
    Essa função calcula a quantidade de pontos de cada time em uma determinada fase
    onde cada fase corresponde a um jogo de ida e um jogo de volta. Cada vitória vale
    3 pontos e cada empate vale 1 ponto.
    Parametro de Entrada: list, list
    Valor de Retorno: Dict
    """
    L3=L1[2]
    L4=L2[2]
    t1=L1[0]
    t2=L1[1]
    times={}
    if L3[0]>L3[1]:
        if L4[1]>L4[0]:
            times[t1] = 6
            times[t2] = 0
            return times
        elif L4[1]==L4[0]:
            times[t1] = 4
            times[t2] = 1
            return times
        else:
            times[t1] = 3
            times[t2] = 3
            return times
    else:
        if L4[1]>L4[0]:
            times[t1] = 3
            times[t2] = 3
            return times
        elif L4[1]==L4[0]:
            times[t1] = 1
            times[t2] = 4
            return times
        else:
            times[t1] = 0
            times[t2] = 6
            return times