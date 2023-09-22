def filtraMultiplos(x,n):
    '''função que cria uma lista com os multiplos de um determinado numero
    list,int -> list'''
    indice = 0
    novalista = ()
    while indice < len(x):
        if x[indice]%n == 0:
            novalista += (x[indice],)
        indice += 1
    return novalista