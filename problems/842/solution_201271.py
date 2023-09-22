def pontos_por_time(ls):
    '''Função que computa os pontos de cada time.
    assinatura: list --> dict
    '''
    ida = ls[0]
    vol = ls[1]
    ret = {ida[0]: 0, ida[1]: 0}
    
    t1 = ida[0]
    t2 = ida[1]
    g1 = ida[2][0]
    g2 = ida [2][1]
    contabilidade(ret, t1, t2, g1, g2)
    
    t1 = vol[0]
    t2 = vol[1]
    g1 = vol[2][0]
    g2 = vol[2][1]
    contabilidade(ret, t1, t2, g1, g2)
    return ret

def contabilidade(d, t1, t2, g1, g2):
    if g1 < g2:
        d[t2] += 3
        
    if g2 < g1:
        d[t1] += 3
        
    if g2 == g1:
        d[t1] += 1
        d[t2] += 1