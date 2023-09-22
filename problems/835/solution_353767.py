def melhor_volta(M):
    '''
    funcao que recebe uma matriz 6x10 de entrada, que marca
    os tempos,em segundos, de cada um dos 6 jogadores, em
    cada uma de suas 10 voltas  e retorna uma tupla com as
    infromacoes de qual foi o corredor mais rapido, qual sua
    volta mais rapida e o tempo dessa volta
    list->tuple
    '''
    rapido=1000
    voltas=1000
    corredor=1000
    for m in range(0,len(M)):
        for n in range(0,len(M[m])):
            if min(M[m][n],rapido)==M[m][n]:
                rapido=min(M[m][n],rapido)
                corredor=m+1
                voltas=n+1
    return corredor,rapido,voltas