def melhor_volta(tempo):
    '''Função que dada uma matriz contendo os tempos de cada volta
    de cada corredor, retorna o corredor que fez o melhor tempo,
    o melhor tempo e a volta que ele fez esse tempo.
    list[int]->tuple(int)'''
    
    melhor=1000
    
    for i in range(len(tempo)):
        for j in range(len(tempo[0])):
            if tempo[i][j] < melhor:
                melhor= tempo[i][j]
                corredor=i
                volta=j
                
    return (corredor+1,melhor,volta+1)