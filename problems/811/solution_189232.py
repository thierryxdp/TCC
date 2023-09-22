def colchao(medidas,h,l):
    '''função que dada as medidas do colchão retorna se é possivel
    ou não a passagem do mesmo pela porta
    float,float,float ->float'''
    a,b,c = medidas
    if (b > h or a > l) and c < l:
        return True
    elif b > h or a > l:
        return False
    else:
        return True