def colchao(m, H, L):
    '''Compara o tamanho do colchão com o tamanho da porta e retorna True 
    se o colchão consegue passar pela porta e False se não consegue.'''
    return m[0] <= H and m[1] <= L or m[1] <= H and m[0] <= L