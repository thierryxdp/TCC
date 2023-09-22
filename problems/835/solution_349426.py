def melhor_volta(matriz_tempos: list)-> tuple:
    """Função que dada uma matriz(6x10) representando respectivamente 6 corredores e 10 voltas
    (com o tempo em segundos a cada volta), retorna o corredor, o tempo e a volta, a quem fez
    a melhor volta."""

    menor_tempo = (matriz_tempos[0][0],matriz_tempos[0][0])

    for corredores in range(0,6,1):
        for voltas in range(0,10,1):
            if matriz_tempos[corredores][voltas] < menor_tempo[1]:
                menor_tempo = (corredores+1,matriz_tempos[corredores][voltas])

    return menor_tempo