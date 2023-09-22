def insere(lista_numero,n):
    """Recebe uma lista com numeros ordenados de forma crescente e um numero n e devolve a lista com este numero dentro dela sem interferir na ordem
    	list, num -> list"""
    lista_numero=list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero