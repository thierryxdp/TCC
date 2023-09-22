def insere(lista_numero,n):
    if n in lista_numero:
        indice = list.index(lista_numero,n)
        list.insert(llista_numero, indice, n)
    elif n < lista_numero[0]:
        list.extend(lista_numero, [n])
    elif n > lista_numero[-1]:
        list.append(lista_numero, [n])
    return lista_numero