def total(lista, produtos):
    '''funcao que, dada uma lista e os produtos disponiveis, retorna o valor total dos produtos contidos na lista;
    list, dict -> int'''
    valor = 0
    listap = list(produtos)
    for item in lista:
        if item in produtos:
            valor = valor + produtos[listap[list.index(listap, item)]]
    return round(valor,2)