def melhor_volta(m):
    '''Função que transforma uma matriz 6 x 10 e calcula a melhor volta, dada 10 voltas de uma corrida de Kart para cada 6 corredores.  
    Mostrando o tempo e a volta.
    list -> tuple'''
    less = qtd = winner = 1000
    for v in range(len(m)):
        for j in range(len(m[v])):
            if min(m[v][j], less) == m[v][j]:
                less = min(m[v][j], less)
                winner = v + 1
                qtd = j + 1

    return winner, less, qtd