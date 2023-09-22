def melhor_volta(matriz):
    ''' funcao que dando uma matriz com os tempos dos corredores
    em cada volta e retornara uma tupla contendo quem teve a 
    melhor volta, em que tempo e em que volta'''
    menor_tempo = volta = vencedor = 10000
    for v in range (0,len(matriz)):
        for t in range (0, len(matriz[v])):
            if min(matriz[v][t],menor_tempo) == matriz[v][t]:
                menor_tempo = min(matriz[v][t], menor_,tempo)
                vencedor = v + 1
                volta = t + 1
            return vencedor, menor_tempo, volta