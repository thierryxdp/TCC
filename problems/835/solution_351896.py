def melhor_volta(m):
    '''
    	essa função recebe uma matriz 6x10 contendo o tempo dos corredores  em cada volta, retornando uma tupla informando 
        de quem foi a melhor volta, tempo e em que volta.
        list-> tuple
    '''
    Linha1 = 0
    Linha2 = 0
    linha3 = m[0][0]
    nLinha = len(m)
    nColuna = len(m[0])
    for i in range(nLinha):
        for j in range(nColuna):
            if (linha3 > m[i][j]):
                linha1 = i+1
                linha2 = j+1
                linha3 = m[i][j]
    return (linha1,linha3,linha2)