def melhor_volta(corredor):
    '''Função que retorna quem fez a melhor volta, com qual tempo e em que volta, list -> tuple'''
    menor_volta = []
    for i in range(6):
        for j in range(10):
            if corredor[i][j] <= menor_volta[i]:
                melhor_volta = i + 1
    return min(melhor_volta)