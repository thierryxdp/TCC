def insere(lista_numero,n):
    '''retorna o numero n na posicao certa segundo a lista de numeros dados em ordem crescente'''
    lista_numero = list.insert(lista_numero, 0, n)
    list.sort([lista_numero])
    str.join(n, lista_numero)
    return lista_numero