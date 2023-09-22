def total(compras, precos):
    '''recebe uma lista e um dicionário, retornando um valor flutuante representando a soma dos preços dos produtos disponíveis na loja
    lista, dicionario -> float
    '''
    preco_total = 0.0
    i = 0
    while (i < len(compras)):
        produto = compras[i]
        if (produto in precos):
            preco_total += dict.get(precos, produto)
        i += 1
    return preco_total