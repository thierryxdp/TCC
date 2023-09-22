def melhor_volta(matriz):
    '''Esta função recebe uma matriz 6x10 com informações
    sobre o tempo de cada corredor e retorna de quem foi a melhor
    volta da prova, com qual tempo e em que volta.
    list -> tupla'''
    
    corredores= len(matriz)
    voltas= len(matriz[0])
    tempo=[]
    teste=[]
    resultado=()
    
    for i in range(corredores):
        for j in range(voltas):
            list.append(tempo,matriz[i][j])
            menor_tempo=min(tempo)
            
        list.append(teste, menor_tempo)
        resultado=min(teste)
        corredor= list.index(teste, resultado)
        volta= list.index(matriz[i][j], resultado)
        
    return (corredor+1, resultado, volta+1)