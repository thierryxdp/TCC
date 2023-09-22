def total(Lcompras, Dpreco):
    """retorna os gastos de uma lista de compras, feitas
    em um dicionario de precos.
    lista, dicionario->float"""
    total=0
    indice=0
    for itens in Lcompras:
        if Lcompras[indice] in Dpreco:
            total= total + Dpreco[Lcompras[indice]]
        indice= indice + 1
    return round(total, 2)