# função que recebe uma lista de compras e um dicionário contendo os preços dos produtos, e retorna o valor total das compras.
#list, dict --> float
def total(lista,produtos):
    valor_total=0
    for i in range(len(lista)):
        if lista[i] in produtos:
            valor=produtos.get(lista[i])
        valor_total+=valor
    return round(valor_total,2)