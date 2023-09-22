def melhor_volta(matriz):
    '''Recebe uma matriz 6x10 com os tempos de cada corredor e
    retorna uma tupla informando de quem foi 
    a melhor volta e qual foi esse tempo;
    list -> tuple'''
    corredor=0
    tempo=matriz[0][0]
    for m in matriz:
        corredor+=1
        volta=0
        for n in m:
            volta+=1
            if n<tempo:
                tempo=n
    return (corredor,tempo,volta)