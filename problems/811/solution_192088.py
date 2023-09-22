def colchao(dim,h,l):
    """dadas as dimensoes de um colchao e as dimensoes de uma porta, retorna 'true' caso o colchao passe e 'false' caso contrario.
list,int,int-> bool"""
    if dim[0]<=h and dim[1]<=l:
        return True
    if dim[1]<=h and dim[0]<=l:
        return True
    else:
        return False