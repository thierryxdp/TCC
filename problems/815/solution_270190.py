def insere(lista_numero, n):
    ''' funcao que insere n na lista ordenada
list, int -> list|| None'''
    if (len(lista_numero)==0):
        return [n]
    elif (n > lista_numero[0]):
        return[lista_numero[0]]+insere(lista_numero[1:],n)
    else:
        return lista_numero[:]