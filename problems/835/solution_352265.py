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
        for i in matriz:
        if min(i)<tempo:
            tempo=min(i)
            corredor=indice
            melhor_volta=i.index(tempo)+1
        indice+=1
    return (corredor, tempo, melhor_volta)