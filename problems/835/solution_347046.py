def melhor_volta(matriz):
    '''funçao que diz a melhor volta numa pista de kart dada uma lista com os tempos'''
    resultado =(0,0,0)
    for corredor in range(6):
        for volta in range(10):
            if matriz[corredor][volta] < resultado[1]:
                resultado = (corredor+1,matriz[corredor][volta],volta+1)
    return resultado