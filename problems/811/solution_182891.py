def colchao(medidas, H, L):
    '''função que calcula e retorna se um colchão passa por uma porta, a partir das medidas dos dois; list, int, int -> bool'''
    
    if H<=(medidas[1] and medidas[2]) or L<=(medidas[1] and medidas[2]):
        return True
    
    elif medidas[1]>(H and L) and medidas[2]>(H and L):
        return False