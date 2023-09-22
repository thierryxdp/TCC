def melhor_volta(corredor):
    '''Função que retorna quem fez a melhor volta, com qual tempo e em que volta, list -> tuple'''
    lista = []
    for i in len(6):
        for j in range(10):
            if lista[i][j] == menor_volta[i]:
                menor_volta = menor_volta + 1
    return min(menor_volta)