def melhor_volta(matriz):
    '''recebe uma matriz 6x10 com os tempos em segundos dos corredores de cada volta.
    retorna uma tupla informando de quem foi a melhor volta, o tempo correspondente
    e em que volta. )Obs: os corredores tem tempos diferentes.
    list --> tupla'''
    
    corredores = []
    
    for i in range(len(matriz)):
        list.append(corredores,min(matriz[i]))
        
    tempo = min(corredores)
    corredor = list.index(corredores, tempo)
    volta = list.index(matriz[corredor],tempo)
    
    return (corredor, tempo, volta)