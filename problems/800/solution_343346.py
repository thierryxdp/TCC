def total(lista_de_compras,produtos):
    '''Função que retorna o valor total dos itens da lista que estão disponíveis, dado a lista de compras e o dicionário dos produtos disponíveis;list,dict->float'''
    soma=0
    for a in lista_de_compras:
        if a in produtos:
            soma=soma+produtos[a]
        if a not in produtos:
            soma=soma+0
    return round(soma,2)