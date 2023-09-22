def insere(lista_numero,n):
    lista_numero.append(n)
    sorted(lista_numero, key=int)
    list.sort(lista_numero)
    return lista_numero