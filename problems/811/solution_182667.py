def colchao (medidas, H, L):
    '''funcao que calcula e retorna as dimensoes dos colchao que Joao pode comprar que passara pela porta
    lista, int, int -> booleano'''
    a = medidas[0]
    b = medidas[1]
    c = medidas[2]
    if (H>=b):
        return True
    elif (H>=c):
        return True
    elif (L>=b):
        return True
    elif (L>=c):
        return True
    else:
        return False