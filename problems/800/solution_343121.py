def total(compras, valores):
    '''a funcao retorna o valor total dos itens da lista
    list, dict-> int'''
    final=0
    for produtos in valores:
        if compras in valores[produtos]:
            final=final+ valores
    return round(final,2)