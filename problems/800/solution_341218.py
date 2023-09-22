def total(lista,produtos):
    """retorna o valor da compra dos itens na lista"""
    """list, dict -> int"""
    
    valor = 0
    for item in lista:
        valor += produtos.get(item)
    return round(valor,2)