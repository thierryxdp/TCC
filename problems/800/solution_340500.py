def total(lista, dicio):
    '''Fazer uma funcao que receba uma lista de compras e um dicionario com o preco de cada produto e retorne o valor total dos itens que estao disponiveis na loja;
    list, dict -> float'''
    
    valor = []
    
    for itens in lista:
        if itens in dicio:
            list.append(valor, dict.get(dicio, itens))
    return round(sum(valor),1)