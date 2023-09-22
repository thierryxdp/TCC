def colchao (dimensao,altura,largura):
    '''Dado as dimensões de do colção de forma crescente, a altura da porta
    e a largura da porta, retorna se o colchão passa (True) ou não (False);
    list,int,int->bool'''
    A,B,C=dimensao
    if  B <= altura:
        return True
    else:
        return False