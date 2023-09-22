def total(lista_de_compras,produtos):
    """Dada uma lista de compras e os produtos catalogados, retorna
    o valor total da compra:
    list,dict-->float"""
    valor=0
    for produto in lista_de_compras:
        if produto in produtos:
            valor+=produtos.get(produto)
    return round(valor,2)