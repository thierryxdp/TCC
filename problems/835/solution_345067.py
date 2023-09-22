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
    return (melhor_piloto,melhor_tempo,0)