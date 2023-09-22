def colchao(medidas, h, l):
    '''dados as medidas do colchão em lista, a altura da porta e sua largura diz se o colchão passa pela porta
    lista, int , int -> booleano'''
    # informações da porta
    altura = h
    largura = l 
    if medidas[1]<= h and medidas[2]<=l:
        return True
    elif medidas[2]<= h and medidas[1]<=l:
        return True
    elif medidas [0]<=h and medidas[1]<=l:
        return True
    elif medidas [1]<=h and medidas[0]<=l:
        return True
    elif medidas[0]<=h and medidas[2]<=l:
        return True
    elif medidas[2]<=h and medidas[0]<=l:
        Return True
    else:
        return False