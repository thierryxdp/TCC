def melhor_volta(matriz):   
    m = matriz
    tempo_individual = m[0][0]
    geral = len(m)
    vencedor = 0
    lista = []
    for i in range(vencedor):
        tempo_corredor = min(m[i])
        if tempo_corredor < m:   
            m = tempo_corredor
            vencedor = i         
    volta = list.index(m[vencedor], tempo_individual)
    return vencedor+1, tempo_individual, volta+1