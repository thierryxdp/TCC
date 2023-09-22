def colchao(tuple,H,L):
    '''Função que retorna se o colchão passa pela porta ou não'''
    a=int(tuple[1])
    if H>=a:
        return True
    else:
        return False