def total(l,b):
    """Função recebe uma lista de compras com os respectivos valores dos itens, e soma o qual será o valor da compra
    list -> int"""
    l =  list(l)
    total = 0
    for i in range(len(l)):
        total = total + (b[l[i]])
    return round(total,2)