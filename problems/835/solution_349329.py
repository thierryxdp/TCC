def melhor_volta(matriz):
    ''' função que dado uma matriz 6x10 com os tempos de cada volta
    dos corredores em segundos, retorna uma tupla informando quem fez a
    melhor volta da prova, com qual tempo e em que volta. list -> tupla'''
    melhor = matriz[0][0]
    for a in range (len(matriz)):
        for b in range (len(matriz[a])):
            if matriz[a][b] < melhor:
                melhor = m[a][b]
                r = (a + 1, melhor, b + 1)
    return r