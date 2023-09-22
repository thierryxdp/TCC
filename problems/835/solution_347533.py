def melhor_volta(matriz):
    '''função que recebe uma matriz 6 x 10 com os tempos dos corredores 
    em cada volta e retorna de quem foi a melhor volta, qual foi o tempo
    e em qual foi a volta. 
    lista -> tupla'''
    #cada linha i corresponde a um corredor
    #cada coluna j representa o tempo de uma volta do corredor da linha i
    
    for i in range(0,5): 
        for j in range(0,9):
            if matriz[i][j] == min(matriz):
                return tempo
            
    return (i+1, tempo, j+1)