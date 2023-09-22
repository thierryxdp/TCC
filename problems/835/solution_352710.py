def melhor_volta(matriz):
    '''docs'''
    
    vencedor = 0
    tempo = 0
    volta = 0
    lista = []
    
    for i in range(len(matriz)):
        
        for j in range(len(matriz[i])):
            lista += [matriz[i][j]]
            tempo = min(lista)
            vencedor = matriz[i].index(tempo)
            volta = 
            
    return vencedor, tempo, volta