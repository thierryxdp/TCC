def pontos_por_time(l):
    '''função de teste'''
    t1=l[0][0]
    t2=l[0][1]
    g1t1=l[0][2][0]
    g1t2=l[0][2][1]
    g2t1=l[1][2][0]
    g2t2=l[1][2][1]
    '''PONTUAÇÃO'''
    if(g1t1>g1t2 or g2t1<g2t2):
        return {t1:3, t2:3}