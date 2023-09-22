def melhor_volta(matriz):
    '''Dado uma matriz 6x10, retorna uma tupla informando de quem foi a melhor prova,com qual tempo e em que volta
    list->tuple'''
    
    tempo=0
    
    for x in range(len(matriz)):
        tempo+=min(matriz[x])