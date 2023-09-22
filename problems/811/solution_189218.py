def colchao(medidas,h,l):
    '''esse colchão passa pela porta? (A,B,C)medidas=centímetros do colchão
H,L=centímetros da porta.
float,float,float,float,float->bool'''
    if h>=a:
        return True
    if l>=b:
        return True
    if h>=b:
        return True
    if l>=a:
        return True
    if h>=c:
        return True
    if l>=b:
        return True
    else:
        return False