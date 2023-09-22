def filtra_pares(x):
    """funçaõ de recebe uma tupla com quatro elementos inteiros como parâmetro e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam."""
    Y=[]
    if X[0]%2==0:
        Y=Y+(X[0],)
        if X[1]%2==0:
            Y=Y+(X[1],)
            if X[2]%2==0:
                Y=Y+(X[2],)
                if X[3]%2==0:
                    Y=Y+(X[3],)
                    return Y