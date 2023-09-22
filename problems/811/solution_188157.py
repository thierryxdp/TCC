def colchao(medidas,h,l):
    """A funçaõ ira retorna True ou False caso um colchão consiga passar, ou não
        por uma porta de dimensões H e L, dado as mesmas e a lista com dimensões
        do colchão D lista(float,float,float)->int,int"""
    if list(medidas)[1] <= H:
        return True
    else:
        return False