def melhor_volta(v):
    '''função que recebe uma matriz voltas v e retorna de quem foi a 
    melhor volta, qual o tempo e em que volta
    list -> tuple'''
    volta = 1000
    for i in range(len(v)):
        for j in range(len(v[0])):
            if v[i][j] < volta:
            	volta = (i+1,v[i][j],j+1)
    return volta