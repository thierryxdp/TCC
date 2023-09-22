# dado um dicionário contendo o preço de cada produto presente na loja
# retorna o valor total dos itens da lista que estejam disponíveis na
# loja
def total(lista,produtos):
    y = 0 
    for x in lista:
        y = y + produtos[x]
    return round(y,2)