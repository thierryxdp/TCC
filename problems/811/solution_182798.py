def colchao(medidas, h, l):
    '''dados as medidas do colchão em lista, a altura da porta e sua largura diz se o colchão passa pela porta
    lista, int , int -> booleano'''
    # informações da porta
    altura = h
    largura = l
    # informações do colchão
    medidas = A, B, C
    if B<=h and C<=l:
        return True
    elif C<=h and B<=l:
        return True
    else:
        return False