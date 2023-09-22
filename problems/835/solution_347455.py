def melhor_volta(matriz: list) -> tuple:
    """Uma pista de Kart permite 10 voltas para cada um dos 6 corredores. Recebe
       uma matriz 6x10 com os tempos em segundos dos corredores em cada volta e
       retorna uma tupla informando de quem foi a melhor volta da
       prova, com qual tempo e em que volta

       Parameters:
       matriz: Matriz 6x10 com os tempos em segudos dos corredores em cada
       volta, representada por lista de lista, na qual cada lista representa uma
       linha e cada lista de lista representa uma coluna

       Return:
       Uma pista de Kart permite 10 voltas para cada um dos 6 corredores. Dado o
       parâmetro "matriz", retorna uma tupla informando de quem foi a melhor
       volta da prova, com qual tempo e em qual volta

       Examples:
       melhor_volta([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16,
       17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33,
       34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
       [51, 52, 53, 54, 55, 56, 57, 58, 59, 60]]) == (1, 1, 1)
    """

    a = min(matriz[0])
    b = min(matriz[1])
    c = min(matriz[2])
    d = min(matriz[3])
    e = min(matriz[4])
    f = min(matriz[5])
    
    lista = [a, b, c, d, e, f]

    melhor_tempo = min(lista)

    corredor = list.index(lista, melhor_tempo)

    volta = list.index(matriz[corredor], melhor_tempo)

    return (corredor + 1, melhor_tempo, volta + 1)