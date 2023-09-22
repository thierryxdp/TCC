def total(lista,precos):
    "função que recebe uma lista de produtos e um dicionario com produtos e preços. Retorna o total gasto para comprar os produtos disponiveis"
    total = 0
    for item in lista:
        if item in precos:
            total += dict.get(item)
    return round(total,2)