def insere(lista_numero, n):
    '''Função que coloque um numero em uma lista continuando a ordem
list,int->list'''
    lista_numero.append(n)
    list.sort(lista_numero)

    return lista_numero