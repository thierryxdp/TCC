def melhor_volta(matriz):
    '''funcao que dado uma matriz 6X10 retorna
    de quem foi a melhor volta,qual o tempo;
    e em que volta; list -> int,int,int'''
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    melhores_tempos = []
    
    for i in range(linhas):
        menores_tempos = min(matriz[i])
        list.append(melhores_tempos,menores_tempos)
    melhor_tempo = min(melhores_tempos)
    melhor_piloto = melhores_tempos.index(melhor_tempo)
    volta = matriz[melhor_piloto].index(melhor_tempo)
    
    #como a contagem comeca no 0 temos que somar +1 para
    #achar o melhor piloto e a melhor volta
    return (melhor_piloto+1,melhor_tempo,volta+1)