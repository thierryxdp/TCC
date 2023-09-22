def total(l, d):
    """Recebe uma lista de compras e um dicionário contendo o preço de cada
produto disponível e retorna o preço da lista.
testes: total(['biscoito', 'sal', 'manteiga'], {'biscoito':3.00, 'sal':0.50, 'manteiga':1.50}) == 5.00
total(['biscoito', 'sal'], {'biscoito':8.50, 'farinha':2.50}) == 8.50
assinatura: list, dict --> int
"""
    ret = []
    for item in l:
        ret += [dict.get(d, item, 0)]
    return round(sum(ret), 2)