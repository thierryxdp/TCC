def melhor_volta(matriz):
    '''Retorna uma tupla indicando a melhor volta, quem a deu e o tempo em que foi concluida
    	list(list) -> tuple(int, float, int)'''
    melhorPessoa = 1
    melhorTempo = matriz[0][0]
    melhorVolta = 1
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] < melhorTempo:
                melhorTempo = matriz[i][j]
                melhorPessoa = i + 1
                melhorVolta = j + 1
    return melhorPessoa, melhorTempo, melhorVolta