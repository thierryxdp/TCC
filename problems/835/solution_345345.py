def melhor_volta(matriz):
    '''recebe uma matriz 6x10 com os tempos em segundos dos corredores em
    cada uma das 10 voltas, e retorna uma tupla informando: De quem foi a 
    melhor volta da prova, com qual tempo e em que volta.
    list ->tuple'''
    minimo = 0
    for i in range(6):
        if minimo ==0 or min(matriz[i]) <minimo:
            minimo =min(matriz[i])
            volta =list.index(matriz[i], minimo) +1
            corredor =i+1
    return corredor, minimo, volta