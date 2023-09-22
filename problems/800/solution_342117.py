def total(lista,produto):
    '''Função que dada uma lista de compras e um dicionario contendo o preço de cada produto, retorna o valor dos itens da lista que estão disponiveis:
    list,dict -> float'''
    soma = 0.00
    i = 0
    for i in lista:
        a = produto[lista[i]]
        soma = soma + a
        i = i + 1
    soma = round(soma,2)
    return soma