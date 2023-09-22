def melhor_volta(matriz):
    '''Recebe como entrada uma matriz com os tempos e 
    segundos dos corredores em cada volta. Ela retorna uma
    tupla com a melhor volta, tempo e em que volta.'''
    melhor_volta= 0
    tempo = 10000
    #Em que volta
    corredor = 0
    #percorre a matriz
    for i in len(matriz):
        #Para coluna dentro da matriz
        for j in range(len(matriz[i])):
            #Verifica se o tempo é maior que o de determinada posição
            if tempo>matriz[i][j]:
                #O tempo é igual ao da posição
                tempo=matriz[i][j]
                #Melhor volta na posição i e j da matriz.
                melhor_volta = matriz[i].index(matriz[i][j])
                corredor=i+1
    return corredor, tempo, melhor_volta