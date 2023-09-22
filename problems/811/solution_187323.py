def colchao(medidas,H,L):
    '''função que retorna se um colchão consegue passar pela porta; list, int, int -> bool'''
    medidas = []
    if medidas[1] <= H:
        return True
    else:
        return False