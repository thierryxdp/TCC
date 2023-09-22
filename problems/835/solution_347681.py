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
            list.append(tempo,matriz[i][j])
            
            
        list.append(tempo_total, tempo)
        resultado=min(teste)
        corredor= list.index(teste, menor_tempo)
        volta= list.index(matriz[corredor], menor_tempo)
        
    return (corredor+1, resultado, volta+1)