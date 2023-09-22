def total (lista,dicionario):
    '''Dado uma lista de comprar e um dicionário com os preços dos produtos em uma loja, retorna o total que será gasto com esses itens
    list, dict->float'''
    preco = 0
    for elemento in range(len(dicionario)):
        if lista[elemento] in dicionario:
            preco = preco + dicionario[dicionario[elemento]]
    return round (preco, 2)