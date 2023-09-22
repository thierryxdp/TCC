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