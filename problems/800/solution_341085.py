def total(compras, preco):
    '''retorna o valor total dos itens da lista de compras'''
    '''lista, dici -> int'''
    
    valor = []
    
    for itens in compras:
        if itens in dicionario:
            list.append(valor, dict.get(preco,itens))
    return round (sum(valor),2)