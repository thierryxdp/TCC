def insere(lista_numero,n):
    if n in lista_numero:
        indice = list.index(lista_numero,n)
        list.insert(lista, indice, n)
    elif n < lista_numero[0]:
        list.extend(lista, n)
    elif n > lista_numero[-1]:
        list.append(lista, n)
    return lista_numero