def filtra_pares (tupla):
    'dado uma tupla com 4 elementos inteiros, retorna uma outra tupla somente com os elementos pares. Tupla -> Tupla'
    tuplaN = ()
    if tupla[0] % 2 == 0:
        tuplaN = tuplaN + (tupla[0],)
    if tupla[1] % 2 == 0:
        tuplaN = tuplaN + (tupla[1],)
    if tupla[2] % 2 == 0:
        tuplaN = tuplaN + (tupla[2],)
    if tupla[3] % 2 == 0:
        tuplaN = tuplaN + (tupla[3],)
    return tuplaN