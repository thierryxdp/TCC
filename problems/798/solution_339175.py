def total(lista_de_compras,produtos):
    soma=0
    for x in lista_de_compras:
        if x in dict.keys(produtos):
             soma+=dict.get(produtos,x)
    return round(soma,2)