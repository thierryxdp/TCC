def colchao(medidas,h,l):
    '''analisa se o colchao com medidas A, B e C consegue passar pela porta de altura h e largura l
    list,int,int -> bool'''
    if (min(medidas[1],medidas[2])) <= h or (min(medidas[1],medidas[2])) <= l:
        return True
    else:
        return False