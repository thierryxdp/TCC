def total(lista,dicionario):
    '''Função para dado uma lista e um dicionario retorna o preço total da compra
    Recebe uma lista de compra e valores
    Retorna o valor total'''
    preco = 0
    for i in lista:
        preco += dicionario[i]
    return round(preco,2)