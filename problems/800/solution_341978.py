def total (lista_compras,preco_produtos):
    """Função que recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível em uma determinada loja e retorna o valor total dos itens da lista que estejam dispoíveis na loja
    entrada: list, dict
    saída: float"""
    valor_total=0
    for produto in lista_compras:
        if produto in preco_produtos:
            valor_total=valor_total+preco_produtos[lista_compras]
    return valor_total