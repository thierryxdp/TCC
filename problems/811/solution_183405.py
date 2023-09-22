def colchao(m,h,l):
    '''Dado as dimensões do colchão, a altura da porta e a largura da porta,
    retorna se você consegue ou não passar com o colchão.
    list,int,int --> bool'''
    A= m[0]
    B= m[1]
    C= m[2]
    
    if B <= h :
        return True
        
    else:
        return False