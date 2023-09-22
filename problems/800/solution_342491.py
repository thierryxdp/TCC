def total(compras,preco):
    '''
    função que recebe uma lista de compras e um dicionario
    contendo o preço de cada produto disponível em uma determinada
    loja
    Retorna o valor total dos itens da lista que estejam disponíveis
    nesta loja.
    '''
    valor=0
    for produto in compras:
        if produto in compras:
            valor += preco[produto]
    return valor