def melhor_volta(matriz):
    '''
       funcao que retorna uma tupla informando
       de quem foi a melhor volta da prova, com 
       qual tempo e em que volta.
       int, int->tuple
    
    '''
    tempo = volta = winer= 1000
    for v in range(0,len(matriz)):
        for t in range(0,len(matriz[v])):
            if min(matriz[v][t],tempo)==(matriz[v][t]):
                tempo=min(matriz[v][t],tempo)
                winer=v+1
                volta=t+1
    return winer, tempo, volta