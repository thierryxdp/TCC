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
            lista_tempos += matriz[i][j] 
            
    lista_tempos = list.sort(lista_tempos)
    menor_tempo = lista_tempos[0]
    onde_esta = matriz.index(menor_tempo)
    
    return (onde_esta, menor_tempo,