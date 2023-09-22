def colchao(medidas,H,L):
    '''função que retorna se o colchão passa pela porta da casa de 
    João ou não.
    lista, int, int -> boolean'''
    
    if medida[1]<H:
        return True
    elif medida[2]<L:
        return True
    elif medida[1]<L:
        return True
    elif medida[2]<H:
        return True
    else:
        return False