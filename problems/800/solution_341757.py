def total(lista_compras,dicionario_produtos):
    '''Função que recebe uma lista de compras e um dicionário
    contendo o preço de cada produto disponível em determinada
    loja, e retorna o valor total dos itens da lista que estejam
    disponíveis nesta loja. list, dict->float'''
    preco_prod = 0
    for i in lista_compras:
        lista=lista_compras[i]
        preco_prod = preco_prod + int(dicionario_produtos.get(lista))
                                       
    return preco_prod