def colchao(medidas,H,L):
    """ função que calcula e retoma se 
    o colchão escolhido passa pela porta de dimensões H e L de entrada
    list int int ->bool"""
    medidas=[A,B,C]
    A=[profundidade]
    B=[altura]
    C=[largura]
    if A>H and C<L:
        return False
    elif A<H and C>L:
        return False
    elif A>H and C>L:
        return false
    else:
        return True