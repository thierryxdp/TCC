def colchao(colchao1,porta):
    '''Dado as dimensões de do colção de forma crescente, a altura da porta
    e a largura da porta, retorna se o colchão passa (True) ou não (False);
    list,int,int->bool'''
    if colchao1[1]>porta[0] and colchao1[1]>porta[1]:
        return False