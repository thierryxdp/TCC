def total(lista_de_compras, produtos):
    """Função que calcula o total gasto numa compra de supermercado a partir dos valores dos produtos"""
    """Parâmetros de entrada: list,dic"""
    """Parâmetros de saída:float"""
    contador=0
    for elemento in lista_de_compras:
        contador+=produtos[elemento]
    return round(contador)