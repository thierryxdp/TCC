def total(lista_de_compras,produtos):
    ''' dada uma lista de compras de uma pessoa e um portifolio de protudos
    de um vendedor, a funcao retornara qnt sera estimado a conta. list, dict float '''
    conta = 0
    for produto in lista_de_compras:
        if produto in produtos:
            conta = conta + produtos.get(produto)
    return round(conta,2)