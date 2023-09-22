def melhor_volta(matriz):
    '''função chamada melhor_volta que receba como entrada uma matriz 6 x 10 com os 
    tempos em segundos dos corredores em cada volta. A função deve retornar uma tupla 
    informando: De quem foi a melhor volta da prova, com qual tempo e em que volta.
    list->tuple
    '''
    tempo=0
    for x in range(len(matriz)):
        for y in range (len(matriz[0])):
            if matriz[x][y]== min(matriz[x]) and min(matriz[x])<tempo:
                corredor=1+x
    			volta=1+y
                tempo=matriz[x][y]  
    return (corredor,tempo,volta)