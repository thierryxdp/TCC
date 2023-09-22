medidas = ([A, B e C])
def colchao(medidas,H,L):
    '''função que retorna se um colchão consegue passar pela porta; list, int, int -> bool'''
    if B <= H or C <= L:
        return True
    else:
        return False