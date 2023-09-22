def melhor_volta(matriz):
    '''funcao que dada uma matriz 6x10 com os tempos em segundos, retorna uma tupla informando:
       De quem foi a melhor volta, com qual tempo e em que volta
       matriz(int) -> tuple(int, int, int)'''
    melhor_volta = matriz[0][0]
    piloto = 1
    num_volta = 1
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < melhor_volta:
                melhor_volta = matriz[i][j]
                piloto = i + 1
                num_volta = j + 1
    return (piloto, melhor_volta, num_volta)