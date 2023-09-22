def total(lista,dicionario):
    """função que retorna o preço das compras baseado em uma lista e um dicionario
    list, dict -> float"""
    compras = 0
    for produto in lista:
        if produto in dicionario:
            compras = compras + dicionario[produto]
        else:
            compras = compras
    return compras