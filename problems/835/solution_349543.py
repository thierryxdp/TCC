def melhor_volta(tempos):
    '''Função que retorna uma tupla com a melhor volta de entrada: list -> tuple'''

    tupla = (0,float('inf'),0)

    for indice1 in range(6):
        for indice2 in range(10):
            if tempos[indice1][indice2] < tupla[1]:
                tupla = (indice1+1,tempos[indice1][indice2],indice2+1)
    return tupla