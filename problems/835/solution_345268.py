# Melhor Volta
def melhor_volta(m):
    '''Ao receber uma matriz 6X10 com os tempos de 6 corredores de Kart,
    a função retornará uma tupla informando qual corredor fez a melhor
    volta, em quanto tempo ele a fez e qual das 10 voltas dele foi a
    campeã;
    LIST -> TUPLE'''
    lvc = []
    lc = []
    lvol = []
    for i in range(0,6):
        m_ = m[i][0]
        for j in range(0,10):
            if(m_> m[i][j]):
                m_= m[i][j]
        lvc.append(m_)
        lc.append(i+1)
        lvol.append(m[i].index(m_)+1)
    mev = min(lvc)
    return (lc[lvc.index(mev)], mev, lvol[lvc.index(mev)])