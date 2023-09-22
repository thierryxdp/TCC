def pontos_por_time(l):
    '''
    A função retorna um dicionário onde a chave é o
    nome do time e o valor é o número de pontos na fase
    (entrada = lista / saída = dicionário)
    '''
    j1 = l[0]
    j2 = l[1]
    t1 = j1[0]
    t2 = j1[1]
    g1 = j1[2]
    g2 = j2[2]
    p1 = 0
    p2 = 0
    if g1[0] > g1[1]:
        p1 = 3
        if g2[1] > g2[0]:
            p1 = p1 + 3
        elif g2[0] == g2[1]:
            p1 = p1 + 1
            p2 = 1
        else:
            p2 = 3
    elif g1[1] > g1[0]:
        p2 = 3
        if g2[0] > g2[1]:
            p2 = p2 + 3
        elif g2[0] == g2[1]:
            p1 = 1
            p2 = p2 + 1
        else:
            p1 = 3
    else:
        p1 = 1
        p2 = 1
        if g2[1] > g2[0]:
            p1 = p1 + 3
        elif g2[0] == g2[1]:
            p1 = p1 + 1
            p2 = p2 + 1
        else:
            p2 = p2 + 3        
    return {t1 : p1, t2 : p2}