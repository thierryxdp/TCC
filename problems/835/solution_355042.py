def melhor_volta(matriz_tempos):
    '''Recebe uma matriz com os 10 tempos dos 6 corredores e retorna de 
    quem foi a melhor volta da prova, com qual tempo e em que volta 
    (list -> tuple)'''
    tempos = ()
    for linha in matriz_tempos:
        for aij in linha:
            tempos = tempos + (aij,)
    melhor_tempo = min(tempos)
    for linha in matriz_tempos:
        for aij in linha:
            if melhor_tempo == aij:
                corredor = (list.index(matriz_tempos[linha])+1)
                volta = (list.index(linha[aij]))+1
    return(corredor,melhor_tempo,volta)