def melhor_volta(matriz):
    '''funcao que dado uma matriz 6X10 retorna
    de quem foi a melhor volta,qual o tempo;
    e em que volta; list -> int,int,int'''
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    melhores_tempos = []
    
    for i in range(linhas):
        for j in range(colunas):
            melhores_tempos = melhores_tempos + [min([matriz[i][j]])]
    melhor_tempo = min(melhores_tempos)
    return (0,melhor_tempo,0)