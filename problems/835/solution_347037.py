def melhor_volta(matriz):
    '''funçao que diz a melhor volta numa pista de kart dada uma lista com os tempos'''
    tempos = []
    for corredor in range(0,len(matriz)):
        for volta in range(0,len(matriz[0])):
            tempos.append(matriz[i][j])       
    return (corredor,matriz[corredor][volta],volta)