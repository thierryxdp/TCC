def melhor_volta(matriz):
    '''Esta função recebe uma matriz 6x10 com informações
    sobre o tempo de cada corredor e retorna de quem foi a melhor
    volta da prova, com qual tempo e em que volta.
    list -> tupla'''
    
    corredores= len(matriz)
    voltas= len(matriz[0])
    tempo=[]
    tempo_total=[]
        
    for i in range(corredores):
        for j in range(voltas):
            menor_tempo=min(matriz)            
        list.append(tempo_total, menor_tempo)
        
        melhor_tempo=min(tempo_total)
        corredor= list.index(tempo_total, menor_tempo)
        volta= list.index(matriz[corredor], menor_tempo)
        
    return (corredor+1, melhor_tempo, volta+1)