def melhor_volta(corredor):
    '''Função que retorna quem fez a melhor volta, com qual tempo e em que volta, list -> tuple'''
    lista = []
    for i in len(6):
        menor_volta = min(corredor)
        for j in range(10):