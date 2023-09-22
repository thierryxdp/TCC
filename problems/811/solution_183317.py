def colchao(M,h,l):
    """dado uma lista com as medidas de uma caixa em formato de paralelepípedo, a altura e a largura de uma porta, diz se a caixa poderá passar pela porta (list[int,int,int],int,int --> bolean"""
    a = M[0] 
    b = M[1] 
    c = M[2] 
    return (a <= h and b <= l) or (a <= l and b <= h) or (a <= h and c <= l) or (a <= l and c <= h) or (c <= h and b <= l) or (c <= l and b <= h)