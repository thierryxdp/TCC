def pontos_por_time(lista1):
    """ A função retorna os pontos de cada time;
    list -> list """
    dic={}
    jogo1 = lista1[0]
    jogo2 = lista1[1]
    t1 = jogo1[0]
    t2 = jogo1[1]
    goals = jogo1[2]

    t1g = goals[0]
    t2g = goals[1]
    if t1g == t2g:
        dic[t1] = 1
        dic[t2] = 1
    if t1g > t2g:
        dic[t1] = 3
        dic[t2] = 0
    if t1g < t2g:
        dic[t1] = 0
        dic[t2] = 3
    
    goals = jogo2[2]
    t2g = goals[0]
    t1g = goals[1]
    if t1g == t2g:
        dic[t1] = dic[t1] + 1
        dic[t2] = dic[t2] + 1
    if t1g > t2g:
        dic[t1] = dic[t1] + 3
        dic[t2] = dic[t2] + 0
    if t1g < t2g:
        dic[t1] = dic[t1] + 0
        dic[t2] = dic[t2] + 3
    return dic