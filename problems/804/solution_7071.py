def filtra_pares(tupla):
    '''Função que retorna os pares dos 4 primeiros números de informação "tupla" = tupla de entrada: tupla -> tupla'''

    n = ()

    if tupla[0] % 2 == 0:
        n = n + (tupla[0],)
    if tupla[1] % 2 == 0:
        n = n + (tupla[1],)
    if tupla[2] % 2 == 0:
        n = n + (tupla[2],)
    if tupla[3] % 2 == 0:
        n = n + (tupla[3],)
    return n