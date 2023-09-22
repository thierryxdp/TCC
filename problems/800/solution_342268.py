def total(l,d):
    """Dada uma lista "l" de compras e um dicionário "d"
    contendo o preço de cada produto disponível, retorna 
    o valor total dos itens disponíveis na loja
    list , dict -> float"""
    produtos = list(d.keys())
    valores = list(d.values())
    valor = []
    for i in range(len(l)):
        for j in range(len(produtos)):
            if l[i] == produtos[j]:
                valor.append((valores[j]))  
    preco = sum(valor)
    return round(preco,2)