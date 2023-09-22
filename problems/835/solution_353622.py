def melhor_volta(corredor):
    '''Função que retorna quem fez a melhor volta, com qual tempo e em que volta, list -> tuple'''
    menor_volta = min(corredor)
    for i in range(6):
        for j in range(10):
              if menor_volta[1] > corredor[i][j]:
                    menor_volta = (i + 1, corredor[i][j], j + 1)
    return menor_volta