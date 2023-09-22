def total(compras,precos):
    """dada uma lista compras de entrada, 
    composta por strings com nomes dos produtos a serem comprados
    e um dicionário preços, contendo como chaves os nomes dos produtos
    e como valores os preços em float,
    retorna qual será o gasto total das compras
    list, dict --> float"""
    valor_total=0
    for produto in compras:
        valor_total=valor_total+precos[produto]
    return round(valor_total,2)