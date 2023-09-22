def melhor_volta(matriz):
    '''Retorna uma tupla informando de quem foi a melhor volta,
    qual tempo e em que volta
    matriz -> tupla'''
    tempo = []
    corredor = 0
    volta = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            tempo += [matriz[i][j]]
    for l in range(len(matriz)):
        for k in range(len(matriz[l])):
            if matriz[l][k] == min(tempo):
                corredor = l
                volta = k
    return corredor, min(tempo), volta