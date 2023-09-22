def total(lista_compras, prods):
    val=0
    for prod in lista_compras:
        val+=round(prods[prod]+0.001, 2)
    return val