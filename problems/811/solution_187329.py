def colchao(medidas,H,L):
    '''função que retorna se um colchão consegue passar pela porta; list, int, int -> bool'''
    if medidas[1] <= H or medidas[2] <= L:
        return True
    else:
        return False