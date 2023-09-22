def maiores(lista_numero, n):
    '''funcao que coloca um numero n em uma lista, ordena ela e depois retorna os numeros maiores que n
    str->str'''
    lista_numero.append(n)
    list.sort(lista_numero)
    x=lista_numero.index(n)
    del(lista_numero[:x+1])
    return lista_numero