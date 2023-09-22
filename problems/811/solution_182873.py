def colchao(medidas, H, L):
    '''função que define se um colchão passa por uma porta de altura H e largura L.
    list, int, int -> bool'''
    
    return (medidas[1] > H) and (medidas[1]>L) and (medidas[2]>H) and (medidas[2]>L)