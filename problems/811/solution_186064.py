def colchao(medidas,h,l):
    '''Retorna se o colchão de medidas a, b e c (sendo a<b<c) passa pela porta de altura h e largura l
list, int, int -> bool'''
    [a,b,c]=medidas
    if ((c>h) and (b>h)) or (a>l):
        return False
    else:
        return True