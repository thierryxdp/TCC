def total(compras, mercado):
    """retorna o valor de uma lista de compras(ldc) baseado em um dicionário(mercado)"""
    valor='mercado'
    for i in compras:
        if i in mercado:
            valor+mercado[i]
            return round(valor,2)