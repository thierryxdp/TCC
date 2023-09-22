#Filtragem
def filtra_pares(X):
    '''Funcao que recebe uma tupla de quatro inteiros e
        que retorna apenas os pares na mesma'''
    s = ()
    if X[0] %2== 0:
        s = s + (X[0],)
        else:
            s = s
            if X[1] %2== 0:
                s = s + (X[1],)
                else:
                    s = s
                    if X[2] %2== 0:
                        s = s +(X[2],)
                        else:
                            s = s
                            if X[3] %2== 0:
                                s = s + (X[3],)
                                else:
                                    s = s
                                    return s