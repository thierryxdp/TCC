def melhor_volta(matriz):
    '''função que recebe uma matriz 6 x 10 com os tempos dos corredores 
    em cada volta e retorna de quem foi a melhor volta, qual foi o tempo
    e em qual foi a volta. 
    lista -> tupla'''
    #cada linha i corresponde a um corredor
    #cada coluna j representa o tempo de uma volta do corredor da linha i
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    lista_tempos = []
    
    for i in range(linhas):
        for j in range(colunas):
            lista_tempos = min(matriz[i][j])
    return lista_tempos