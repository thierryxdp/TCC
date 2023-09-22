def melhor_volta(corredor):
    '''Função que retorna quem fez a melhor volta, com qual tempo e em que volta, list -> tuple'''
    for i in range(6):
        for j in range(10):
            menor_volta = min(corredor[i])
            if corredor[i][j] <= menor_volta[i]:
                menor_volta = i + 1
                menor_volta = j + 1
                menor_volta = corredor[i][j]
    return