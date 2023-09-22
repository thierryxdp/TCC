def ida(g1,g2):
    timeA=0
    timeB=0
    if g1>g2:
        timeA=3
    elif g1==g2:
        timeA=1
        timeB=1
    else:
        if g1<g2:
            timeB=3
def volta(g3,g4):
    if g3>g4:
        timeB=timeB+3
    elif g3==g4:
        timeA=timeA+1
        timeB=timeB+1
    else:
        if g3<g4:
            timeA=timeA+3
            
def pontos_por_time([[c1,v1,[g1,g2]],[c2,v2,[g3,g4]]]):
    return {x,timeA,y,timeB}