def melhor_volta(matriz):
    '''Recebe uma matriz 6x10 com os tempos de cada corredor e
    retorna uma tupla informando de quem foi 
    a melhor volta e qual foi esse tempo;
    list -> tuple'''
    corredor=0
    tempo=matriz[0][0]
    volta=0
    for m in matriz:
        if min(m)<tempo:
            tempo=min(m)
            corredor=list.index(matriz,m)
            volta=list.index(m,min(m))
    return (corredor+1,tempo,volta+1)