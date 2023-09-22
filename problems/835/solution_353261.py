def melhor_volta(matriz):
    '''Retorna uma tupla indicando a melhor volta, quem a deu e o tempo em que foi concluida
    	list(list) -> tuple(int, float, int)'''
    melhorPessoa = 1
    melhorTempo = matriz[0][0]
    melhorVolta = 1
    for i in range(matriz):
        for j in range(matriz):
            if matriz[i][j] < melhorTempo:
                melhorTempo = matriz[i][j]
                melhorPessoa = i
                melhorVolta = j
    return melhorPessoa, melhorTempo, melhorVolta