def total(lista_compras, prods):
    val=0
    for prod in lista_compras:
        val+=prods[prod]
    valc=round(val, 2)
    return valc