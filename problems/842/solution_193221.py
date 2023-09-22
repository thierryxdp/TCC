def pontos_por_time(l):
    l1,l2=l
    g1=l1[2]
    g2=l2[2]
    p1=0
    p2=0
    if g1[0]>g1[1]:
        p1=p1+3
    elif g1[0]<g1[1]:
        p2=p2+3
    else:
        p1=p1+1
        p2=p2+1
    if g2[0]<g2[1]:
        p1=p1+3
    elif g2[0]>g2[1]:
        p2=p2+3
    else:
        p1=p1+1
        p2=p2+1
    return {l1[0]:p1,l1[1]:p2}