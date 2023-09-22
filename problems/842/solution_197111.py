def pontos_por_time(l):
    '''função de teste'''
    t1=l[0][0]
    t2=l[0][1]
    g1t1=l[0][2][0]
    g1t2=l[0][2][1]
    g2t1=l[1][2][0]
    g2t2=l[1][2][1]
    T=[t1,t2]
    A=T+[[g1t1]+[g1t2]]
    B=T+[[g2t2]+[g2t1]]
    '''primeiro jogo'''
    p1t1=0
    p1t2=0
    if(g1t1>g1t2):
        return 3+p1t1
    if(g1t1<g1t2):
        return 3+p1t2
    if(g1t1==g1t2):
        return p1t1+1;p1t2+1
    '''segundo jogo'''
    p2t1=0
    p2t2=0
    if(g2t1>g2t2):
        return 3+p2t1
    if(g2t1<g2t2):
        return 3+p2t2
    if(g2t1==g2t2):
        return p2t1+1;p2t2+1
    if(p1t1+p2t1>p1t2+p2t2):
        return {t1:p1t1+p2t1, t2:p1t2+p2t2}
    else:
        return {t2:p1t2+p2t2, t1:p1t1+p2t1}