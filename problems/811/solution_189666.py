# list, int, int -> booleano 
def colchao(medidas,H,L):
    """
    Essa função calcula se o colchão passará pela porta
    ou se não passará. 'Medidas' é uma lista onde seus 
    elementos correspondem as medidas do colchão (a,b,c).
    'H' corresponde a altura da porta e 'L' corresponde a
    largura da porta.
    """
    m=sorted(medidas)
    m1=m[0]
    m2=m[1]
    m3=m[2]
        
    if m1<H and m2<L:
        return True 
    elif m1<H and m2>L:
        return False
    elif m1<H and m2==L:
        return False
    elif m1>H and m2<L:
        return False
    elif m1==H and m2<L:
        return False
    elif m1>H and m2>L:
        return False
    elif m1==H and m2==L:
        return False