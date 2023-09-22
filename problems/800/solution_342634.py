def total(lista, dicionario):
    '''
        Funcao que recebe uma lista de compras e um dicionario
        contendo o preco de cada produto disponivel em uma 
        determinada loja,e retorna o valor total dos itens que
        estejam disponiveis nesta loja
        list, dicio -> float
    '''
    total = 0
    for produto in lista:
        total += dicionario[lista]
    return round(total, 2)