def melhor_volta(matriz):
    '''Dada uma matriz 6x10 com os tempos em segundos
    de 6 corredores em 10 voltas de uma corrida, retorna
    uma tupla com o corredor que desempenhou a melhor
    volta, qual seu tempo e em que volta
    list -> list'''
    menores_tempos = []
    for i in range(len(matriz)):
        menores_tempos.append(min(matriz[i]))
    
    menor_tempo = min(menores_tempos)
    corredor = menores_tempos.index(min(menores_tempos))
    melhor_volta = matriz[corredor].index(menor_tempo)
    return (corredor, menor_tempo + 1, melhor_volta + 1)