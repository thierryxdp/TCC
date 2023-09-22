def melhor_volta(matriz):
    '''Programa que retorna uma tupla com o melhor da prova, menor tempo e em qual volta foi o menor tempo
    list -> tuple'''
    
    c = range(6)
    v = range(10)
    t = (0,float('inf'),0)
    
    for i in c:
        for j in v:
            if matriz[i][j] < t[1]:
               t = (i+1, matriz[i][j], j+1)
    return t