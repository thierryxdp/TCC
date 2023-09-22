def insere(lista_numero,n):
    """ a crescenta um número interio n em uma lista e o coloca em ordem;list,int->list"""
    lista= lista_numero+[n]
    lista1= list.sort(lista)
    return (lista1)