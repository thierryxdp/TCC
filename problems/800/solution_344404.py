def total(lista, dicionario):
    '''função que recebe uma lista de compras e um dicionário contendo os preços de cada produto de uma loja, a fução deve retornar o valor detodos os itens da lista de compras que estão disponiveis na loja'''
    soma = 0
    for item in lista:
        soma = soma + dicionario[item] 
    return round(soma,2)