def melhor_volta(matriz_tempos):
    """ a função retorna os valores de quem teve a melhor volta e com qual tempo foi"""
    tupla = (0,float('inf'),0)
    for i in range(6):
        for j in range(10):
            if matriz_tempos[i][j] < tupla[1]:
                tupla = (i+1,matriz_tempos[i][j],j+1)
    return tupla