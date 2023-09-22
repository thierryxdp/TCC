def melhor_volta (matriz):
    """Função que dado uma matriz 6x10 com os tempos em segundos dos
    corredores em cada volta, retorne qual corredor teve a melhor volta
    da prova, com qual tempo e em que volta.
    lista -> tuple"""

    corredor = 0
    tempo = 999999999
    volta = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if tempo > matriz[i][j]:
                tempo = matriz[i][j]
                corredor = i
                volta = j
    return corredor, tempo, volta