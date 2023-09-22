def total(lista, dicionario):
    """Dados uma lista de compra de produtos e um dicionário com todos os produtos e seus valores de uma
    loja, a função calcula quanto custará para comprar todos os produtos da lista de compras;
    list, dict -> float"""
   	valor = 0
    for produtos in lista:
        valor = valor + dicionario[produto]
    return round(valor)