def total(lista_de_compras, produtos):
    custo = 0
    
    for x in lista_de_compras:
        if x in produtos:
            custo += produtos[x]
            
    return round(custo,2)