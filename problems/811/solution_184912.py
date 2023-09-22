def colchao(lista,h,l):
    '''Dado as dimensões de do colção de forma crescente, a altura da porta
    e a largura da porta, retorna se o colchão passa (True) ou não (False);
    list,int,int->bool'''
    colchao=lista[0]
    porta=lista[1]
    
   
    if (porta<=h and colchao<=l) or (porta<=l and colchao<=h):
        return True
    else:
        return False