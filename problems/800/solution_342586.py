def total(lista1,dic1):
    '''função que, dada uma lista de compras e
    um dicionário contend o preço de cada produto, 
    disponível em uma determinada loja, retorna 
    o valor total dos itens da lista que estejam
    disponíveis nesta loja.
    list, dic -> float'''
    soma = 0
    for produto in lista1:
        if produto in dic1:
            soma = soma + dic1[produto]
    return soma