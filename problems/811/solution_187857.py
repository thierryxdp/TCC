def colchao(medidas,h,l):
    '''
    retorna se o tamanho do colchao passa pela porta
    list,int -> bool
    '''
    if (medidas[0]*medidas[1])> h*l:
        return True
    else:
        return False