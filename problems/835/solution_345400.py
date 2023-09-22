def melhor_volta(matriz):
    m0=min(matriz[0])
    m1=min(matriz[1])
    m2=min(matriz[2])
    m3=min(matriz[3])
    m4=min(matriz[4])
    m5=min(matriz[5])
    m_tds=min([m5,m4,m3,m2,m1,m0])
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if m_tds == matriz[i][j]:
                return i+1,m_tds,j+1