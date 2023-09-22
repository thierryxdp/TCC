def total(compras,preco):
    """pega os produtos da lista de compras e utiliza o dicionario de preco
    para somar o total
    lista, dicionario -> int"""
    t=0
    for c in preco:
        if c in compras:
            t+=preco[c]
    return round(t,2)