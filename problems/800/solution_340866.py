def total(lista,produtos):
    '''Função que recebe uma lista de compras e um um dicionario de produtos
    e retorna o valor total dos itens da lista que estejam disponíveis na loja
    list,dict -> float
    '''
    soma_produtos = 0
    for i in range(len(lista)):
        soma_produtos = soma_produtos + produtos[lista[i]]
    return round(soma_produtos,2)