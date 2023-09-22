def melhor_volta(matriz):
    '''função chamada melhor_volta que receba como entrada uma matriz 6 x 10 com os 
    tempos em segundos dos corredores em cada volta. A função deve retornar uma tupla 
    informando: De quem foi a melhor volta da prova, com qual tempo e em que volta.
    list->tuple
    '''
    corredor=1
    volta=1
    tempo=0
    for x in range(len(matriz)-1):
        for y in range (len(matriz[0])-1):
            if matriz[x][y]== min(matriz[y]):
                tempo=matriz[x][y]
                corredor+=x
                volta+=y
    return (corredor,tempo,volta)