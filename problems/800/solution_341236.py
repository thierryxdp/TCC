def total(p,dic):
    """Função que recebe uma lista de compras(p) e um dicionário(dic) contendo o preço de cada produto disponível em uma determinada loja, e retorna o valor total dos itens da lista que estejam disponíveis na loja"""
    """list,dict->int"""
    s=0
    for y in range(len(p)):
        if p[y] in list(dict.keys(dic)):
            s=s+dict.get(dic,p[y])
    return round(s,2)