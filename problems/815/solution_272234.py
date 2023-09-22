def insere(lista_numero, n):
    '''Dada uma lista e um numero n, retorna os numeros maiores que n em ordem crescente
    '''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero