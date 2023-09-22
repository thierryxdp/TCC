def melhor_volta (tempos):
    '''Dada uma matriz com os tempos dos corredores a cada volta, retorna uma tupla dizendo quem foi a melhor volta da prova, o tempo e em qual volta'''
    voltas_corre=list.copy(tempos)
    corredores=len(tempos)
    voltas = len(tempos[0])
    melhor_volta=voltas_corre[0][0]
    for i in range(corredores):
        for j in range(voltas):
            if voltas_corre[i][j]<= melhor_volta:
                melhor_volta=voltas_corre[i][j]
                corredor=i+1
                volta= j+1
    return(corredor, melhor_volta, volta)