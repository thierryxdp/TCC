def melhor_volta(matriz):
    '''Retorna uma tupla informando quem foi o vencedor da prova.
    list-->tuple'''
    melhor=0
    tempo=0
    lista=[]
    
    for i in matriz:
        for j in range(len(i))):
            lista+=matriz[i][j]
            
        tempo=min(tempo)
        
    if tempo in matriz:
        melhor=matriz[j].index(tempo)
        
    return melhor