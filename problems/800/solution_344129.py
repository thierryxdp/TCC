def total(lista_compras, produto_disp):
    """Retorna o valor total de um lista de compras dado os preços dos produtos disponíveis no mercado;
    list, list -> float"""
    valor_total = 0
    for produto in lista_compras:
        if produto in list(produto_disp.keys()):
            valor_total += produto_disp[produto]
    return round(valor_total,2)