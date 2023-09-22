def melhor_volta(matriz):
    '''
    
    
    '''
    tempo=v=winer=1000
    for i range(0,len(matriz)):
        for t in range(0,len(matriz[i])):
            if min(matriz[i][t],tempo)==matriz[i][t]:
                tempo=min(matriz[i][t],tempo)
                winer=i+1
                v=t+1
        return winer,tempo,v