def pontos_por_time(lista):
    '''Recebe uma lista com duas listas, cada uma contendo informações sobre o jogo de ida e volta entre dois times (nome dos dois times e placar do jogo no formato [time1, time2, [A,b]) e retorna um dicionáriocujos mapeamentos são nome do time e número de pontos feitos na fase; lista -> dicionário'''
    a = lista[0]
    ak = a[2]
    g1t1, g1t2 = ak[0], ak[1]
    b = lista[1]
    bs = b[2]
    g2t1, g2t2 = bs[0], bs[1]
    time1, time2 = a[0], a[1]
    #jogo 01
    if g1t1 > g1t2:
        p1 = 3
        p2 = 0
    elif g1t1 == g1t1:
        p1 = 1
        p2 = 1
    else:
        p1 = 0
        p2 = 3
    #jogo 02
    if g2t1 > g2t2:
        pp1 = 3
        pp2 = 0
    elif g2t1 == g2t2:
        pp1 = 1
        pp2 = 1
    else:
        pp1 = 0
        pp2 = 3
    pontos1, pontos2 = (p1 + pp1), (p2 + pp2)
    return {time1:pontos1, time2:pontos2}