def melhor_volta(tempo):
    '''teste'''
    
    melhor=1000
    
    for i in range(len(tempo)):
        for j in range(len(tempo[0])):
            if tempo[i][j] < melhor:
                melhor= tempo[i][j]
                corredor=i
                volta=j
                
    return (corredor+1,melhor,volta+1)