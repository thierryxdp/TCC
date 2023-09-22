def melhor_volta(m_tempos):
    
    tupla = (0,float('inf'),0)
    for l in range(6):
        for c in range(10):
            if m_tempos[l][c] < tupla[1]:
                tupla = (l+1,m_tempos[l][c],c+1)
    return tupla