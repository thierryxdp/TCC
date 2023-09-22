def total (lista_compras, produtos):
    '''Recebe uma lista de compras e um dicionário contendo o preço
    de cada produto e calcula o valor total dos itens disponíveis;
    list [str], dict {str: float} -> float'''
    soma=0
    for item in lista_compras:
        valor = dict.get(produtos,item)
        soma = soma + valor
    return round(soma,2)