def colchao(medidas,h,l):
    """retorna a condicao do colchao passar pela porta
    dados a medida do colchao e a altura/largura da 
    porta. 
    OBS: as medidas devem ser as mesmas.
    list,float,float->bool"""
    b=int (medidas[1])
    c=int (medidas[2])
    if b<=l:
        return True
    elif c<=h:
        return True
    else:
        return False