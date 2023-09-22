def melhor_volta(matriz):
    '''Dada uma matriz de voltas de Kart, retorna qual foi o melhor corredor, seu tempo e em qual das 10 voltas ele foi melhor.
    list -> tuple'''
    menor = matriz[0][0]
    piloto = 1
    volta = 1
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < menor:
                menor = matriz[i][j]
                piloto = i+1
                volta = j+1
    return menor, piloto, volta