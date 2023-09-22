def colchao(medidas,h,l):
    '''
    retorna se o tamanho do colchao passa pela porta
    list,int -> bool
    '''
    if medidas[2]<h and medidas[1]<l and (medidas[0]*medidas[1]*medidas[2])>h*l:
        return True
    else:
        return False