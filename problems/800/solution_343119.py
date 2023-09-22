def total(lista, dicionario):
    '''
    Função que recebe uma lista de compras e um dicionário com os valores
    dos produtos em um supermercado, retorna o total da compra.
    list, dict -> int
     '''
    soma = 0
    for produto in lista:
        soma += dicionario[produto]
    return soma