#inclue um número na lista, de forma que ela continue ordenada
def insere(lista_numero,n):
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero