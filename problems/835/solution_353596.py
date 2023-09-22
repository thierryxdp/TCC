def melhor_volta(corredor):
    '''Função que retorna quem fez a melhor volta, com qual tempo e em que volta, list -> tuple'''
    menor_volta = []
    for i in range(6):
        for j in range(10):
            if corredor[i][j] <= menor_volta[i]:
                menor_volta = i + i
    return min(menor_volta)