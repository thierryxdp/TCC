def insere(lista_numero, n):
    '''função que dadas uma lista ordenada crescente de números e um numero n,
       retorna a lista com o número n incluso na posição correta. lista, int -> lista'''
    lista = list.sort(lista_numero)
    list.insert(lista, n, n)
    return lista