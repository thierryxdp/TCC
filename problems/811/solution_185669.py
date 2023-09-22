def colchao(medidas,h,l):

    """Função que dado as medidas do colchão e da porta retorna

    se há passagem pela porta ou não. int, int, int -> string"""

    a, b, c = medidas[0], medidas[1], medidas[2]

    

    if a<=h and b<=l:

        return True

    if a<=h and c<=l:

        return True

    if b<=h and a<=l:

        return True

    if b<=h and c<=l:

        return True

    if c<=h and a<=l:

        return True

    elif c<=h and b<=l:

        return True

    return False