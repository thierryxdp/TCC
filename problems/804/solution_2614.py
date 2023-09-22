def filtra_pares(tupla):
    '''recebe uma tupla e devolve uma nova tupla somente com os números pares
    tupla de int -> tupla de int'''
    a, b, c = tupla
    a = tupla[0]
    b = tupla[1]
    c = tupla[2]
    d = tupla[3]
    nova_tupla = []
    if a%2 ==0:
        resposta = resposta + (a,)
    if b%2 ==0:
        resposta = resposta + (b,)
    if c%2 ==0:
        resposta = resposta + (c,)
    if d%2 ==0:
        resposta = resposta + (d,)