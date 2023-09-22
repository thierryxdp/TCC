def colchao (medidas,H,L):
    '''
    função que define se um determinado colchão passa por uma porta a partir de determinadas medidas
    list, int, int -> bool
    '''
    if medidas[1] > H:
        return False
    if medidas[1] < H or medidas[2] < L or medidas[1] == H and medidas[2] < L:
        return True