def insere(lista_numero,n):
    ''' dado uma lista e um inteiro, a funçao retorna uma lista ordenada desses numeros, list,int->list'''
    lista1=lista_numero+[n]
    list.sort(lista1)
    return lista1