def melhor_volta(m):
    '''recebe como entrada uma matriz 6 x 10, onde são
    6 corredores e 10 voltas, retornando de quem foi a 
    melhor volta, com qual tempo e em qual volta
    list(list) -> tuple'''
    
    corredores = []
    voltas = []
    tempos_min = []
    
    for i in m:
        corredores += [i,]
        tempos_min += min(i)
        
    return corredores