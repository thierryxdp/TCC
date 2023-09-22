def insere(lista_numero, n):
    '''funcao que insere um numero em uma lista e coloca a lista em ordem
    str->str'''
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero