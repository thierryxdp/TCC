def total(lista_de_compras, produtos):
    """funcao que recebe de entrada uma lista de compras e 
    um dicionario contendo o preco de cada produto disponivel
    em uma determinada loja, e retorna o valor total dos itens
    da lista que estejam disponiveis nesta loja;
    list, dict -> float"""
    
    valor_total = 0
    for i in lista_de_compras:
        if i in produtos:
            valor_total = valor_total + produtos[i]
    return round(valor_total,2)