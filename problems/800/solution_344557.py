def total(compras, precos):
    '''recebe uma lista e um dicionário, retornando um valor flutuante representando
    a soma dos preços dos produtos disponíveis na loja.
    lista, dicionario -> float
    '''
    preco_total = 0.0
    for produto in compras:
        if (produto in precos):
            preco_total += dict.get(precos, produto)
    return preco_total