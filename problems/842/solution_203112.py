#Start your python function here
def pontos_por_times(ls):
    t1=ls[0[0]]
    t2=ls[0[1]]
    g1i=ls[0[2[0]]]
    g2i=ls[0[2[1]]]
    g1v=ls[1[2[1]]]
    g2v=ls[1[2[0]]]
    pt1=0
    pt2=0
    if g1i>g2i:
        pt1=pt1+3
    elif g1i<g2i:
        pt2=pt2+3
    elif g1i=g2i:
        pt1=pt1+1
        pt2=pt2+1
    if  g1v>g2v:
        pt1=pt1+3
    elif g1v<g2v:
        pt2=pt2+3
    elif g1v=g2v:
        pt1=pt1+1
        pt2=pt2+1
    return {t1:pt1,t2:pt2}