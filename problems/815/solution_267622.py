def insere(lista_numero,n):
    if n in lista_numero:
        indice = list.index(lista_numero,n)
        list.insert(llista_numero, indice, n)
    elif n < lista_numero[0]:
        lista_numero = [n]+lista_numero
    elif n > lista_numero[-1]:
        list.extend(lista_numero, [n])
    return lista_numero