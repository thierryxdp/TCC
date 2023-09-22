def colchao(m,H,l):
    '''Dado as medidas do colchao e o tamanho da porta, calcula
    se o colchão passa pela porta. list[int,int,int],int,int ->
    bool'''
    if m[0] <= max(H,l) and m[1] <= max(H,l):
        return True
    else:
        return False