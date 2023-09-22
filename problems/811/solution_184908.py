def colchao(h,l):
    '''Dado as dimensões de do colção de forma crescente, a altura da porta
    e a largura da porta, retorna se o colchão passa (True) ou não (False);
    int,int->bool'''
    colchao,porta=lista[0],lista[1]
    if (porta<=h and colchao<=l) or (porta<=l and colchao<=h):
        return True
    else:
        return False