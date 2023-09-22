def total(lista_de_compra,produtos):
    ''' funcao recebe uma lista de produtos a serem comprados
    e uma lista com seus respctivos preços, dic, dic-->float'''
    preco=[]
    for i in produtos:
        if lista_de_compra in produtos[i]:
            preco+= list(dic.valves(meses))
    return sum(preco)