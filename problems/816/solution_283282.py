#
#
#
#
def maiores(lista_inteiros,n):
    list.append(lista_inteiros,n)
    list.sort(lista_inteiros)
    i=list.index(n)
    lista_inteiros=lista_inteiros[-1:i:-1]
    list.reverse(lista_inteiros)
    return lista_inteiros