def total(lista_de_compras, produtos):
    '''Funcao recebe uma lista de produtos e um dicionario contendo produtos de uma loja com seus respetivos precos e retorna o valor total a ser gasto para a compra dos produtos
list -> dict'''
    valorTotal = 0
    for i in lista_de_compras:
        if (i in dict.keys(produtos)):
            valorTotal += dict.get(produtos, i)
    return round(valorTotal, 2)