def insere(lista_numero,n):
    """ A função retornar uma lista modificada com elementos maiores que n;
    list, int -> list """
    list.sort(lista_numero)
    addint = lista_numero + [n,]
    return addint