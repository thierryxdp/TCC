def melhor_volta(m):
    '''	
    	essa função recebe uma matriz 6x10 com os tempos em segundos dos corredores em cada volta e retorna
        uma tupla informando quem foi a melhor volta, o melhor tempo e em que volta
        list->tuple
    '''
    nLinha = len(m)
    nColuna= len(m[0])
    linha1 = 0
    linha2 = 0
    for i in range(nLinha):
        for j in range(nColuna):
            if (m[0][0] > m[j][i]):
                linha1 = i+1
                linha2 = j+1
                m[0][0] = m[j][i]
    return linha1,linha2,m[0][0]