def total(lista,dicionario):
    """Uma função que receba uma lista de compras contento o valor
    de cada prodto disponível, que retorne o valor total dos itens
    que estejam disponíveis"""
    v = 0
    for P in range(len(lista)):
        x = lista[P]
        if y in dict.keys(dicionario):
            v = v + dict.get(dicionario,i)
    return round(v,2)