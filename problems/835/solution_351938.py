def melhor_volta(m):
    '''
    	essa função recebe uma matriz 6x10 contendo os tempos dos corredores em cada volta; e retorna uma tupla informando
        de quem foi a melhor volta, com qual tempo e em que volta
        list-> tuple
    '''
    linha = []
    nLinha = len(m)
    nColuna = len(m[0])
    for i in range(nLinha):
        linha.append(min(m[i]))
        menor = min(linha)
        if menor in m[i]:
            quem = m.index(m[i])+1
            qual = m[i].index(min(linha))+1
            
    return (quem, menor, qual)