def total (lista_compras,dict_precos):
    '''Função que recebe uma lista de compras e um dicionário contendo o preço de cada produto, e retorna o valor total dos itens da lista que estejam disponíveis.
    list, dict -> float'''
    valor_tot = 0
    contador = 0
    for contador in range(len(lista_compras)):
        if lista_compras[contador] in dict_precos:
            valor_tot = valor_tot + dict.get(dict_precos,lista_compras[contador])
        contador = contador + 1
    return round(valor_tot,2)