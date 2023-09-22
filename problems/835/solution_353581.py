def melhor_volta(corredor):
    '''Função que retorna quem fez a melhor volta, com qual tempo e em que volta, list -> tuple'''
    menor_volta = 0
    for i in len(6):
        i = i + 1
        for j in len(10):
            if corredor < menor_volta[i]:
                menor_volta = menor_volta + 1
    return menor_volta