def melhor_volta(matriz):
    '''Função que retorna o melhor tempo, qual corredor e a melhor
       volta. Lista - > tuple'''
    L = []
    a = 0    
    for c in matriz:
        a = min(c)
        list.append(L,a)
    corredor = L.index(min(L))
    volta = matriz[corredor].index(min(L))
    return (corredor+1,min(L),volta+1)