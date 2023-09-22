def insere(lista_numero, n):
    '''Esta lista insere um número "n" em uma lista "lista_numero" em seu local correto seguindo uma ordem crescente.
list,float->list'''
    lista_numero.insert(0,n)
    list.sort(lista_numero)
    return lista_numero