def total(lista, produtos):
    aux=0
    for x in lista:
    	aux+=produtos[x]
    return round (aux,2)
""" recebe uma lista de compras e um dicionário com os preços de produots e retorna o valor total
da compra"""