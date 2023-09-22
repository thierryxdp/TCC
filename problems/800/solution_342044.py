def total(l,d):
    '''
    Recebe uma lista e um dicionário. Varre a lista e no
    produto p, verifica o valor dele. Insere esse valor
    no somatório e arredonda para duas casas decimais.
    '''
    s = 0
    for p in l:
        v = d[p]
        s += v
        s = round(s,2)
    return s