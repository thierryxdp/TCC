def total(lista,dicionario):
    '''funcao que dada uma lista e um dicionario retorna o valor total dos items presentes na lista. list, dict --> float'''
    preco = 0
    for produtos in lista:
        preco += dicionario[produtos]
    return preco