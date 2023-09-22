def filtra_pares(tupla):
    '''Função que, dados quatro elementos inteiros como parâmetro, retorna um tupla contendo apenas os elementos pares da tupla original na mesma ordem que se encontravam; int, int, int, int -> tuple.'''
    pares = ()
    
    if (tupla[0] % 2 == 0):
        pares = pares + (tupla[0],)
    if (tupla[1] % 2 == 0):
        pares = pares + (tupla[1],)
    if (tupla[2] % 2 == 0):
        pares = pares + (tupla[2].)
    if (tupla[3] % 2 == 0):
        pares = pares + (tupla[3],)
    return pares