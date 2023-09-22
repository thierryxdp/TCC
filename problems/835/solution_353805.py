def melhor_volta(voltas):
    ''' funcao que dada uma matriz 6x10 com as 10 voltas dos 6 corredores ela retorne uma tupla dizendo de quem foi a melhor volta ,o menor tempo e em que volta ocorreu
    list->tuple'''
    melhortempo=()
    for i in range(len(voltas)):
        for j in range(len(voltas)):
             voltas[i][j]
            for k in range(len(min(voltas))):
                 melhortempo=(i,min(voltas[i]),j)
    return melhortempo