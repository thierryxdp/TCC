def colchao(medidas,H,L):
    '''função que retorna se o colchão passa pela porta da casa de 
    João ou não.
    lista, int, int -> boolean'''
    
    if medidas[1]<H:
        return True
    elif medidas[2]<L:
        return True
    elif medidas[1]<L:
        return True
    elif medidas[2]<H:
        return True
    else:
        return False