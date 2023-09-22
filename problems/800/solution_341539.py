def total(lista_de_compras, produtos):
    '''Retorna o valor total do preco dos itens da
    lista de compra presentes no dicionario produtos
    list, dict --> float'''
    valor = 0
    for i in lista_de_compras:
        if i in produtos:
            valor = valor + produtos[i]
    return round(valor,2)