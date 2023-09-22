def filtra_pares(tupla):
    '''recebe uma tupla e devolve uma nova tupla somente com os números pares
    tupla de int -> tupla de int'''
    a = tupla[0]
    b = tupla[1]
    c = tupla[2]
    d = tupla[3]
    nova_tupla = []
    if a%2 ==0:
        nova_tupla = nova_tupla + [a,]
    if b%2 ==0:
        nova_tupla = nova_tupla + [b,]
    if c%2 ==0:
        nova_tupla = nova_tupla  + [c,]
    if d%2 ==0:
        nova_tupla = nova_tupla  + [d,]
    return nova_tupla