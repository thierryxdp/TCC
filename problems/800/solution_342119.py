def total(lista,produto):
    '''Função que dada uma lista de compras e um dicionario contendo o preço de cada produto, retorna o valor dos itens da lista que estão disponiveis:
    list,dict -> float'''
    soma = 0.00
    indice = 0
    while indice<len(lista):
        a = produto[lista[indice]]
        soma = soma + a
        indice = indice + 1
    soma = round(soma,2)
    return soma