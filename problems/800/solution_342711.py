def total(l,d):
    '''
    	A função recebe um lista de compras e um dicionário que relaciona os produtos
        disponíveis num mercado com seus preços. Com isso, ela retorna a soma dos 
        preços dos produtos da lista disponíveis nesse mercado. O valor total terá
        uma aproximação de duas casas decimais.
        l -> list (lista de compras, cotém apenas os nomes dos produtos)
        d -> dict (relaciona produtos disponíveis num mercado e seus preços)
        list, dict -> float
    '''
    v_total = 0
    for chave in l:
        if chave in d:
            v_total += d[chave]
    v_total = round(v_total,2)
    return v_total