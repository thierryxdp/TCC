def total(lista_compras,tabela_loja):
    '''Esta função recebe uma lista de compras e um catálogo de um supermercado, e retorna o valor total dss compras.
list,dict->int'''
    i=0
    valor=0
    for i in range(len(lista_compras)):
        if lista_compras[i] in tabela_loja:
            valor+= tabela_loja[lista_compras[i]]
    return round(valor,2)