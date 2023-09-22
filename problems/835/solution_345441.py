def melhor_volta(matriz):
    '''Dada uma matriz 6x10 com 6 corredores e 10 tempos, retorna quem teve a melhor volta, em quanto tempo a volta foi e em qual volta foi
   matriz de int -> tuple'''
    tupla = (0,float('inf'),0)
    for i in range(6):        
        for j in range(10):            
            if matriz[i][j] < tupla[1]:
            tupla = (i+1,matriz[i][j],j+1)
    return tupla