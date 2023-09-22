def insere(lista_numero,n):
    n=list(n,)
    list.extend(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero