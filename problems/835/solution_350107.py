def melhor_volta(matriz6x10):
    '''Faça uma funcao que receba uma matriz 6x10 com os tempos em
    segundos dos corredores em cada volta, e retorne uma tupla informando
    quem foi a melhor volta da prova, com qual tempo e em que volta.
    list-->tuple.'''
    melhorVolta = (0, matriz6x10[0][0],0)
    for corredor in range(6):
        for volta in range(10):
            if matriz6x10[corredor][volta] < melhorVolta[1]:
                melhorVolta=(corredor+1,matriz6x10[corredor][volta],volta+1)
    return melhorVolta