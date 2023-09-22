def pontos_por_time(ls):
    '''Função que computa os pontos de cada time na fase
    representada por /fase/
    assinatura: list -> dict'''
    # nome dos times
    t1 = ls[0][0]
    t2 = ls[1][0]
    
    #inicializando um dicionário de retorno
    ret = {}
    ret[t1] = 0
    ret[t2] = 0
    
    gols_t1 = ls[0][2][0] #gols do t1
    gols_t2 = ls[0][2][1] #gols do t2
    contabiliza(ret, t1, gols_t1, t2, gols_t2)
    
    gols_t1 = ls[1][2][1]
    gols_t2 = ls[1][2][0]
    contabiliza(ret, t1, gols_t1, t2, gols_t2)
    return ret