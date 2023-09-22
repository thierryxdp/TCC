def melhor_volta(matriz):
    '''Dada uma matriz 6x10 com 6 corredores e 10 tempos, retorna quem teve a melhor volta, em quanto tempo a volta foi e em qual volta foi
   matriz de int -> tuple'''
    tupla = (0,float('inf'),0)
    for u in range(6):
        for k in range(10):
        if matriz[u][k] < tupla[1]:
        tupla = (u+1,matriz[u][k],k+1)
    return tupla