def ida(g1,g2):
    if g1>g2:
        return [3,0]
    elif g1==g2:
        return [1,1]
    else:
        if g1<g2:
            return [0,3]
def volta(g3,g4):
    if g3>g4:
        return [0,3]
    elif g3==g4:
        return [1,1]
    else:
        if g3<g4:
            return [3,0]
            
def pontos_por_time([[c1,v1,[g1,g2]],[v1,c1,[g3,g4]]]):
    timeA=ida(g1,g2)[0]+volta(g3,g4)[0]
    timeB=ida(g1,g2)[1]+volta(g3,g4)[1]
    return {'c1','timeA','v1','timeB'}