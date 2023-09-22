def filtra_pares(tupla):
    '''funçao que, fornecidos quatro numeros inteiros em forma de tupla,
   retorna uma nova tupla contendo apenas os elementos pares da original,
   na mesma ordem fornecida
   tupla -> tupla'''
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