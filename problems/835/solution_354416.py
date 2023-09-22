def melhor_volta(matriz):

    '''Função que dada uma pista de Kart permite 10 voltas para cada um dos 6
corredores, recebe como entrada uma matriz 6 X 10 com os tempos em segundos dos
corredores e retorna  uma tupla informando de quem foi a melhor volta da prova,
com qual tempo e em que volta. 
list -> tuple '''
    
    menort = 1000
    volta = 1000
    vencedor = 1000
    for v in range(0, len(matriz)):
        for t in range(0, len(matriz[v])):
            if min(matriz[v][t], menort) == matriz[v][t]:
                menort = min(matriz[v][t], menort)
                vencedor = v + 1
                volta = t + 1
    return vencedor, menort, volta