def total(lista, produtos):
    'Função que recebe uma lista de produtos e um cátalogo de preços e retorna o preço total dos itens da lista.'
    'list, dict->float'
    soma=0
    for item in lista:
        if item in list(dict.keys(produtos)):
            soma=soma+dict.get(produtos,item)
    return round(soma,2)