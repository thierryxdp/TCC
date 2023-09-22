def total(lista_de_compra,produtos):
    ''' funcao recebe uma lista de produtos a serem comprados
    e uma lista com seus respctivos preços, dic, dic-->float'''
    preco=0
    for i in produtos:
        if i in lista_de_compra:
            preco= preco+produtos[i]
    return round(preco,2)