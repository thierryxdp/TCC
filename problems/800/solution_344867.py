# Total
def total(lista,precos):
    """Esta função recebe uma lista de itens normalmente encontrados em supermercados e os precos referentes a cada produto e soma os valores
    list -> int"""
    lista = list(lista)
    total = 0
    for i in range(len(lista)):
        total = total + (precos[lista[i]])
    return round(total,2)