def melhor_volta(matriz):
    '''Recebe uma matriz 6x10 com os tempos de cada corredor e
    retorna uma tupla informando de quem foi 
    a melhor volta e qual foi esse tempo;
    list -> tuple'''
    corredor=0
    tempo=0
    for m in matriz:
        volta=0
        for n in m:
            volta+=1
            if n<tempo:
                tempo=n
                corredor=m+1
    return (corredor,tempo,volta)