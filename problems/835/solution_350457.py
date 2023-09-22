def melhor_volta(x):
    '''
    funcao retorna de quem foi a melhor volta, o tempo e a volta que se destacou
    x==matriz de entrada 6x10, reespectivamente 6 corredores e 10 voltas
    '''
    volta=(0,float('inf'),0)
    p=6
    h=10
    for i in range(p):
        for j in range(h):
            if x[i][j]<volta[1]:
                volta=(i+1,x[i][j],j+1)
    return volta