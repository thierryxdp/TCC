def melhor_volta(M):
    '''
    funcao que determina a melhor volta de corredores de uma pista de kart, em que o numero de linhas determina a quantidade de corredores (6) e o numero de colunas determino a quantidade de voltas (10)
    parametros:
    M--->list
    saida:
    str
    '''
    tempos_min=[]
    for i in range(len(M)):
        tempos_min.append(min(M[i]))
        corredor=tempos_min.index(min(tempos_min))+1
        tempo=min(tempos_min)
        volta=M[corredor-1].index(tempo)+1
    return (corredor,tempo,volta)