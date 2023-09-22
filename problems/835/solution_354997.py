def melhor_volta(matriz):
    '''Recebe uma matriz 6x10 contendo os tempos(s) dos corredores em cada 
    volta e retorna uma tupla informando quem teve a melhor volta, em que 
    tempo e em qual volta;
    list->tuple'''
    
    menor_tempo=volta=vencedor=1000
    for v in range(0, len(matriz)):
        for t in range(0, len(matriz[v])):
            
            if min(matriz[v][t], menor_tempo) == matriz[v][t]:
                menor_tempo = min(matriz[v][t], menor_tempo)
                vencedor = v + 1
                volta = t + 1
    return vencedor, menor_tempo, volta