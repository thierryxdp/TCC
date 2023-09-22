def total(lista,dicionario):
    """Uma função que receba uma lista de compras contento o valor
    de cada prodto disponível, que retorne o valor total dos itens
    que estejam disponíveis"""
    v = 0
    for p in range(len(lista)):
        x = lista[p]
        if x in dict.keys(dicionario):
            v = v + dict.get(dicionario,i)
    return round(v,2)