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