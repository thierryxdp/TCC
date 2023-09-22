def total(compras,precos):
    """
    Função que recebe uma lista de compras e um dicionário com os preços
    dos produtos de um supermercado e retorna o valor total da compra
    
    list, dict -- > float
    """
    
    valor = 0
    
    for produto in compras:
        
        valor += precos[produto]
    return valor