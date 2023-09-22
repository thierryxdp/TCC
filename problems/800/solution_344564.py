def total(lista,dic):
    preco=0
    for prod in lista:
            preco=dic[prod]+preco
    return preco