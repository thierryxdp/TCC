def total(lista,preco):
    """Retorna o preco necessario para comprar a lista de compras;
    	list,dic -> float"""
    total = 0
    for palavra in lista:
        if palavra in preco:
            total = total + preco[palavra]
    return round(total, 2)