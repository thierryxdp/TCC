def total(lista_de_compras, produtos):
    ''' list, dict -> int ''' 
    resultado = 0
    valor = 0
    for resultado in range(len(lista_de_compras)):
        if lista_de_compras[resultado] in produtos:
            valor += produtos[lista_de_compras[resultado]]
    return round (valor,2)