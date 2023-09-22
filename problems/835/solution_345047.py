def melhor_volta(matriz):
    '''Função que dada uma matriz 6x10 com os tempos em segundos dos corredores
em cada volta, retorna uma tupla informando: De quem foi a melhor volta da prova,
com qual tempo e em que volta.
    list -> tuple(str,float,int)
    '''
    campeao=1
    melhor_volta = matriz[0][0]
    volta = 1
    for i in range(len(matriz)):
        melhor_volta_parcial = min(matrizes[i])
        if melhor_volta_parcial < melhor_volta:
            melhor_volta = melhor_volta_parcial
            campeão = i+1
            volta = list.index(matri[i],melhor_volta)+1
    return (campeao,melhor_volta,volta)