def total(x,y):
    """Função que recebe uma lista de compras e um dicionário
    contendo o preço de cada produto disponível em uma determinada
    loja e retorna o valor total dos itens da lista.
    lista -> lista"""
    lista1 = ['']
    lista2 = {'',':',''}
    for iten in x:
        if y in x[iten]:
            lista1 = lista1 +[iten]
    return sum(lista1)