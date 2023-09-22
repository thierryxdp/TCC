def colchao(m,h,l):
    '''Dado as dimensões do colchão, a altura da porta e a largura da porta,
    retorna se você consegue ou não passar com o colchão.
    list,int,int --> bool'''
    A= m[0]
    B= m[1]
    C= m[2]
    a = A<=h and A<=l
    b = B<=h and B<=1
    c = C<=h and C<=l
    
    if a==b==c or a==b or a==c or b==c:
        return True
    else:
        return False