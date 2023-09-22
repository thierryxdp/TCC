def total(lista,tabela):
    '''função que recebe uma lista de compras e uma tabela de precos e rotrna o valor total dos itens disponíveis. list -> int'''
    lista = list(lista)
    total = 0
    for i in range (len(lista)):
        total = total + (tabela[lista[i]])
    return round(total,2)