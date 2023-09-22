def melhor_volta(matriz):
    '''função  que dada uma matriz 6x10 retorna o menor tempo 
    junto com de quem foi a melhor volta e em que volta
    list->list'''
    #Descobrindo o tempo da melhor volta
    tempos=[]
    for i in range(6):
        tempos=tempos+matriz[i]
    tempo=min(tempos)
    for i in range(6):
        for j in range(10):
            if matriz[i][j]==tempo:
                corredor=i+1
                volta=j+1
                return (corredor,tempo,volta)