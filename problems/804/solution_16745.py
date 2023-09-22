def filtra_pares(a,b,c,d):
    '''
    Recebe 4 valores inteiros em uma ordem determinada.
    Abre uma tupla vazia. Adiciona os valores na ordem,
    caso eles sejam considerados pares.
    int, int, int, int -> tuple
    '''
    t = ()
    if a % 2 == 0:
        t.append(a)
    if b % 2 == 0:
        t.append(b)
    if c % 2 == 0:
        t.append(c)
    if d % 2 == 0:
        t.append(d)
    return t