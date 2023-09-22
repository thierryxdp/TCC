#Filtragem
def filtra_pares(X):
    '''Funcao que recebe uma tupla de quatro inteiros e
        que retorna apenas os pares na mesma'''
    t =()
    if X [0] %2 == 0:
        t = t +(X[0],)
        else:
            t = t
            if X[1] %2 == 0:
                t = t +(X[1],)
                else:
                    t = t
                    if X[2] %2 == 0:
                        t = t +(X[2],)
                        else:
                            t = t
                            if X[3] %2 == 0:
                                t = t +(X[3],)
                                else:
                                    t = t
                                    return t