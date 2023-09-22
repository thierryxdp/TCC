def melhor_volta(matriz):
    '''essa funçao recebe uma matriz 6x10 representando os corredores e o numero de voltas 
    e retorna em uma tupla quem fez a melhor volta, em qual tempo e qual foi essa volta
    list -> tupla'''
    menor_tempo= min(matriz[0][0], matriz[0][1])
    corredor=1
    volta= list.index(matriz[0], menor_tempo)+1
    
    return volta