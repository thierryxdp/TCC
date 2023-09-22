def melhor_volta(matriz):
    '''Recebe uma matriz com as 10 corridas de 6 corredores e retorna
    uma tupla informando quem teve a melhor volta, com qual tempo ele
    a completou e qual das voltas foi a melhor
    mat->tuple'''
    menor=[]
    volta=[]
    for corredor in matriz:
        menor=menor+[min(corredor)]
        volta=volta+[list.index(corredor,min(corredor))]
    melhor_corredor=list.index(menor,min(menor))+1
    melhor_tempo=min(menor)
    melhor_volta=volta[melhor_corredor-1]
    return (melhor_corredor,melhor_tempo,melhor_volta)