def total(lista,mercado):
    """Função que recebe uma lista de compras e retonra o valor total dos itens
    list,dict-->float"""
    preco = 0
    for produto in lista:
        if produto in mercado:
            preco += mercado[produto]
        return preco