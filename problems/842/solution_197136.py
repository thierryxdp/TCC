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
    if(g1t1+g2t1>g1t2+g2t2):
        return {t2:6, t1:0}
    elif(g1t1+g2t1<g1t2+g2t2):
        return {t1:6, t2:0}