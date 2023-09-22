def melhor_volta(matriz):
    """ A função melhor_volta, recebe como entrada uma matriz 6 x 10 com os tempos em segundos dos corredores em cada volta e retornar uma tupla informando de quem foi a melhor volta da prova, com qual tempo e em que volta.
        
        Parameters:
        matriz = matriz 6x10 de numeros inteiros (representantes dos tempos dos corredores, em segundos) a ser analisada

        Testes:
            melhor_volta ([[88, 60, 62, 26, 93, 13, 74, 9, 54, 1], [43, 64, 72, 35, 2, 65, 97, 7, 57, 84], [95, 69, 76, 94, 53, 8, 75, 96, 31, 44], [36, 98, 16, 71, 59, 99, 19, 30, 46, 100], [18, 58, 49, 89, 37, 14, 82, 66, 51, 77], [85, 87, 17, 50, 67, 90, 63, 47, 22, 101]]) == (1, 1, 10)
            melhor_volta ([[26, 81, 39, 97, 19, 10, 51, 31, 22, 41], [15, 30, 7, 95, 5, 50, 20, 91, 56, 88], [65, 82, 87, 62, 77, 21, 3, 99, 1, 8], [92, 23, 89, 48, 38, 66, 9, 98, 83, 2], [6, 33, 16, 49, 11, 45, 12, 28, 46, 60], [68, 53, 44, 27, 42, 86, 13, 94, 4, 52]]) == (3, 1, 9)

        Returns:
            uma tupla informando de quem foi a melhor volta da prova, com qual tempo e em que volta.
            list --> tuple
    """
    nlin = len(matriz)
    ncol = len(matriz[0])
    menor_tempo = 99999999
    for i in range(nlin):
        if menor_tempo>min(matriz[i]):
            menor_tempo = min(matriz[i])
    for i in range(nlin):
        for j in range(ncol):
            if matriz [i][j] == menor_tempo:
                return (i+1,menor_tempo,j+1)