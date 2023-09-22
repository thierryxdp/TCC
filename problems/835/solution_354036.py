def melhor_volta(matriz):
    '''
    função que recebe uma matriz 6x10 que contém os tempos
    em segundos de corredores de uma pista de Kart.
    A função retorna uma tupla informando de quem foi a 
    melhor volta da prova, o tempo desse corredor e e em 
    que volta foi esse melhor tempo
    list -> tuple
    '''
    tempo = 1000
    volta = 1000
    corredor = 1000
    tempo = volta = corredor
    
    for v in range(0, len(matriz)):
        for t in range(0, len(matriz[v])):
            if min(matriz[v][t], tempo) == matriz[v][t]:
                tempo = min(matriz[v][t], tempo)
                corredor = v + 1
                volta = t + 1

    return corredor, tempo, volta