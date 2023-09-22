def melhor_volta(m):
    '''Função que transforma uma matriz 6 x 10 e calcula a melhor volta, dada 10 voltas de uma corrida de Kart para cada 6 corredores.  
    Mostrando o tempo e a volta.
    list -> tuple'''
    less = qtd = winner = 1000
    for i in range(len(m)):
        for j in range(len(m[i])):
            if min(m[i][j], less) == m[i][j]:
                less = min(m[i][j], less)
                winner = v + 1
                qtd = t + 1

    return winner, less, qtd