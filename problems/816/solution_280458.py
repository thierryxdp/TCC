def maiores(lista, n):
    '''Função que que retorna a lista só com os numeros maiores que o indicado
list,int->list'''
    lista.append(n)
    list.sort(lista)
    list.reverse(lista)
    a = list.index(lista, n)
    del lista[a:]
    list.reverse(lista)

    return lista