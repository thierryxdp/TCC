def melhor_volta(matriz):
    '''Retorna quem deu a melhor volta, seu tempo e qual volta foi
    	list(list) -> tuple(int, int, int)'''
    melhorTempo = matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            tempo = matriz[i][j]
            if tempo < melhorTempo:
                melhorTempo = tempo
                melhorCorredor = i + 1
                melhorVolta = j + 1
    return melhorCorredor, melhorTempo, melhorVolta