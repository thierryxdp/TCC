def total(lista_compras,dicionario_produtos):
    '''Função que recebe uma lista de compras e um dicionário
    contendo o preço de cada produto disponível em determinada
    loja, e retorna o valor total dos itens da lista que estejam
    disponíveis nesta loja. list, dict->float'''
    preco_prod = 0
    for i in lista_compras:
        preco_prod = preco_prod + dicionario_produtos.get(i)
                                       
    return round(preco_prod,2)