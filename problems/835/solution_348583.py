def melhor_volta(m):
    '''Recebe como entrada uma matriz 6 x 10 com os tempos em segundos
    dos corredores em cada volta e retorna uma tupla informando: De
    quem foi a melhor volta da prova, com qual tempo e em que volta
    list->tuple '''

    menor = []
    for corredor in range( len(m)):
        menor = min(m[corredor])[0]
       
    for i in range (len(menor)):
        if (menor[i] < menor[i+1]):
        	melhor = menor[i]
            
    return melhor