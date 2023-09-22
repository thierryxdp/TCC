def total(lista,itens):
    """Retorna o valor dos itens da lista presentes na loja dado tal lista e os itens.
    list,dic->float"""
    v=0
    for c in lista:
        if c in list(dict.keys(itens)):
            v+=itens[c]
        else:
            v=v
    return round(v,2)