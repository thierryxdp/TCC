def filtra_pares(tup):
    'função que recebe uma tupla e retorna seus números pares'
    par = ()
    if tup[1]%2==0:
        par+=tup[1]
        if tup[2]%2==0:
            par+=tup[2]
            if tup[3]%2==0:
                par+=tup[3]
                if tup[4]%2==0:
                    par+=tup[4]
                    return par