def total(lista_compras,valores):
    """Funca que retorna o valor total das compras dados a lista
    de compras e o preco de cada produto
    list, dict --> float"""
    valor = 0
    for i in range(len(lista_compras)):
        x = valores[lista_compras[i]]
        valor = valor + x/1
    return valor