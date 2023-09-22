def colchao(medidas,h,l):
    """Função que recebe as medidas do colchão e da porta e retorna
    se ele passa pela porta"""
    a, b, c = medidas[0], medidas[1], medidas[2]
    
    if a<=h and b<=l:
        return True
    elif a<=h and c<=l:
        return True
    elif b<=h and a<=l:
        return True
    elif b<=h and c<=l:
        return True
    elif c<=h and a<=l:
        return True
    elif c<=h and b<=l:
        return True
    return False