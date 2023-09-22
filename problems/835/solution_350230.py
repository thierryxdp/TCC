def melhor_volta(matriz):
    '''Dada uma matriz 6x10 com os tempos em segundos
    de 6 corredores em 10 voltas de uma corrida, retorna
    uma tupla com o corredor que desempenhou a melhor
    volta, qual seu tempo e em que volta
    list -> list'''
    menores_tempos = []
    for i in range(len(matriz)):
        menores_tempos += min(matriz[i])
    menor_tempo = menores_tempos.index(min(menores_tempos))
    return menor_tempo