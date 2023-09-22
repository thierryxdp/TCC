def total(lista_compras,dicionario):
    '''funcao que recebe uma lista de compras e um dicionario
    contendo o preco de cada produto disponivel em uma
    determinada loja, e retorna o valor total dos itens
    da lista que estejam disponiveis nesta loja
    list,dicionario->float'''
    valortotal=0
    for elementos in lista_compras:
        if elementos in dicionario:
            valortotal= valortotal + math.ceil(dicionario[elementos],2)
    return valortotal