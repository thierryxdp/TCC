def total(lista_de_compras,produtos):
    """Função retorna o valor total de uma lista de compras dado os produtos disponiveis na loja;
        list, dict -> float"""
    valor = 0
    lista_disponiveis = list(preco_dos_produtos.keys())
    for produto in lista_de_compras:
        if produto in lista_disponiveis:
            valor += preco_dos_produtos[produto]
    return round(valor,2)