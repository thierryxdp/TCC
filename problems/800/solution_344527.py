#list, dict -> float
def total(lista_compras, prods):
    #criar a variável para o preço da compra
    val=0
    #calcular o preço da compra
    for prod in lista_compras:
        val+=prods[prod]
    valc=round(val, 2)
    return valc