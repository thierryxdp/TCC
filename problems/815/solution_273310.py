def insere(lista_numero, n):
    """ Define uma função que dada uma lista, adiciona uma lista e então retorna uma lista ordenada """
    ordenada = lista_numero.append(n)
    list.sort(ordenada)
    return ordenada