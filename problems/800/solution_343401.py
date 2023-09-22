def total (compras, mercado):
    """Função que recebe uma lista de compras e um dicionário
    contendo o preço de cada produto disponível em uma
    determinada loja, e retorna o valor total dos itens da 
    lista que estejam disponíveis nesta loja.
    list, dict -> float"""
    valor = 0
    for i in compras:
        if i in mercado:
            valor = valor + mercado[i]
    return round(valor,2)