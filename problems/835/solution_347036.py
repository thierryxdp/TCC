def melhor_volta(matriz):
    '''funçao que diz a melhor volta numa pista de kart dada uma lista com os tempos'''
    tempos = []
    corredor = 1
    for i in range(0,len(matriz)):
        volta = 0
        for j in range(0,len(matriz[0])):
            tempos.append(matriz[i][j])
            volta += 1 
    corredor += 1        
    return (min(tempos),volta)